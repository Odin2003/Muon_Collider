import fastjet as fj
import ROOT
from pyLCIO import IOIMPL
import math
import signal

# Input LCIO file for Background
#file_path = "/lustre/work/odschnei/mu_mu_a_j_j/background_1000GeV_Gamma/reco/output_reco_run102.slcio"
file_path = "/home/odschnei/USMCC/mu_mu_a_j_j/background_1000GeV_Gamma/reco/output_reco_run102.slcio"
output_file = "histograms_background.root"

# Timeout handler function
def timeout_handler(signum, frame):
    raise TimeoutError("Event processing time exceeded 15 minutes.")

signal.signal(signal.SIGALRM, timeout_handler)

def delta_r(p1, p2):
    eta1 = 0.5 * math.log((p1.E() + p1.pz()) / (p1.E() - p1.pz()))
    eta2 = 0.5 * math.log((p2.E() + p2.pz()) / (p2.E() - p2.pz()))
    phi1 = math.atan2(p1.py(), p1.px())
    phi2 = math.atan2(p2.py(), p2.px())
    delta_eta = eta1 - eta2
    delta_phi = math.fmod(phi1 - phi2 + math.pi, 2 * math.pi) - math.pi
    return math.sqrt(delta_eta**2 + delta_phi**2)

def calculate_girth(jet):
    jet_eta = jet.eta()
    jet_phi = jet.phi()
    jet_pt = jet.pt()
    girth = 0.0
    for constituent in jet.constituents():
        pt_i = constituent.pt()
        eta_i = constituent.eta()
        phi_i = constituent.phi()
        delta_eta = eta_i - jet_eta
        delta_phi = math.fmod(phi_i - jet_phi + math.pi, 2 * math.pi) - math.pi
        delta_r = math.sqrt(delta_eta**2 + delta_phi**2)
        girth += (pt_i / jet_pt) * delta_r
    return girth

# Initialize histograms
histograms = {
        "dR_bs": ROOT.TH1F("dR_bs_background", "Delta R (b, bbar) Background; dR; Counts", 50, 0, 4),
        "girth": ROOT.TH1F("girth_background", "Jet Girth Background; Girth; Counts", 50, 0, 1),
        "jet_mass": ROOT.TH1F("jet_mass_background", "Jet Mass Background; Mass [GeV]; Counts", 15000, 0, 3000),
        "jet_pt": ROOT.TH1F("jet_pt_background", "Jet pT Background; pT [GeV]; Counts", 15000, 0, 3000),
        }

reader = IOIMPL.LCFactory.getInstance().createLCReader()
reader.open(file_path)
print(f"Processing file: {file_path}")

R = 0.8
jet_def = fj.JetDefinition(fj.antikt_algorithm, R)

for event in reader:
    try:
        signal.alarm(15 * 60)  # Set the alarm for 15 minutes
        print(f"Processing Event: {event.getEventNumber()}")

        collection = event.getCollection("MCParticle")
        particles = []
        b_quark, bbar_quark = None, None

        #Cap events for debugging
        #if event.getEventNumber() > 9:
            #break

        for mc in collection:
            momentum = mc.getMomentum()
            px, py, pz = momentum[0], momentum[1], momentum[2]
            energy = mc.getEnergy()
            particles.append(fj.PseudoJet(px, py, pz, energy))
            pid = mc.getPDG()
            parents = mc.getParents()
            for parent in parents:
                parent_pid = parent.getPDG()
                if pid == 5 and abs(parent_pid) == 9000005:
                    b_quark = fj.PseudoJet(px, py, pz, energy)
                if pid == -5 and abs(parent_pid) == 9000005:
                    bbar_quark = fj.PseudoJet(px, py, pz, energy)

        if b_quark and bbar_quark:
            dR_bs = delta_r(b_quark, bbar_quark)
            histograms["dR_bs"].Fill(dR_bs)
        else:
            print(f"Event {event.getEventNumber()}: Missing b or bbar quark")

        collection = event.getCollection("PandoraPFOs")
        particles = []
        # Create a list to store particles from jets with mass > 5 GeV
        selected_particles = []


        for pfo in collection:
            momentum = pfo.getMomentum()
            px, py, pz = momentum[0], momentum[1], momentum[2]
            energy = pfo.getEnergy()
            particles.append(fj.PseudoJet(px, py, pz, energy))

        sequence = fj.ClusterSequence(particles, jet_def)
        jets = sequence.inclusive_jets(ptmin=20.0)

        for jet in jets:
            jet_mass = jet.m()
            jet_pt = jet.pt()
            print("jet mass: ", jet_mass)
            girth = calculate_girth(jet)
            if jet_mass > 10.0:
                histograms["jet_mass"].Fill(jet_mass)
                histograms["jet_pt"].Fill(jet_pt)
                print("jet_pt: ", jet_pt)
                histograms["girth"].Fill(girth)
                # Add the constituents of this jet to the selected_particles list
                for constituent in jet.constituents():
                    selected_particles.append(constituent)
            else:
                print("photon jet pt: ", jet_pt)
                histograms["jet_mass"].Fill(jet_mass)
                histograms["jet_pt"].Fill(jet_pt)

        signal.alarm(0)  # Cancel the alarm


        # Now calculate the combined invariant mass from all selected particles.
        # Sum the four-momentum components:
        total_px = sum(p.px() for p in selected_particles)
        total_py = sum(p.py() for p in selected_particles)
        total_pz = sum(p.pz() for p in selected_particles)
        total_energy = sum(p.e() for p in selected_particles)

        # Compute the invariant mass using m^2 = E^2 - (px^2 + py^2 + pz^2)
        invariant_mass = math.sqrt(max(total_energy**2 - (total_px**2 + total_py**2 + total_pz**2), 0.0))
        print("invariant mass: ", invariant_mass)
        histograms["jet_mass"].Fill(invariant_mass)

    except TimeoutError as e:
        print(f"Skipping Event {event.getEventNumber()} due to timeout: {e}")
        signal.alarm(0)

reader.close()

output_file = ROOT.TFile(output_file, "RECREATE")
histograms["jet_mass"].Write()
histograms["jet_pt"].Write()
histograms["dR_bs"].Write()
histograms["girth"].Write()
output_file.Close()

print(f"Histograms saved to '{output_file}'")

