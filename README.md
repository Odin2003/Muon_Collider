# Muon Collider
This roughly follows the tutorials found at https://mcd-wiki.web.cern.ch/software/tutorials/fermilab2024/ with event generation being done by MadGraph5 and Pythia. The .hepmc file produced through pythia is then inserted at the "Detector Simulation" step of the CERN 2023 tutorial. After the simulation part, the steps follow the Fermilab 2024 tutorial. All parts should be followed on the **HPCC**:

```
ssh -X -Y {USERNAME}@login.hpcc.ttu.edu
```

Then get all the files from this repository using

```
git clone https://github.com/Odin2003/Muon_Collider.git
cd Muon_Collider
```

## Event Generation
### MadGraph 5
Generating events is done with MadGraph5. Here I will describe the process to generate events for muon collisions in which an Axion-Like Particle (ALP) and a photon are produced. The ALP consequently decays to $b ~ \bar{b}$ quarks:

<div align="center">
  <img width="200" alt="image" src="https://github.com/user-attachments/assets/e2531751-7770-47f1-a42e-499d2eeeca67" />
</div>  
<br>


Create a software folder and inside download the MadGraph software from https://launchpad.net/mg5amcnlo :

```
mkdir software
cd software
wget https://launchpad.net/mg5amcnlo/3.0/3.6.x/+download/MG5_aMC_v3.5.8.tar.gz
tar -xvf MG5_aMC_v3.5.8.tar.gz
```

Create a conda environment on HPCC with python and root:

```
conda create -n my_root_env python=3.9
conda activate my_root_env
conda install -c conda-forge root
```

We will need the version of pythia8 we use in madgraph to match the one in our conda environment. Check this using

```
pythia8-config --version
```

This should return a version like 8.312. Then get the .tgz file corresponding to this version from the pythia8 website https://pythia.org/releases/ using wget (replace 8312 if your conda environment has a different pythia8 version).

```
wget https://pythia.org/download/pythia83/pythia8312.tgz
```


Now we can start setting up MadGraph5. Within MG5_aMC_v3_5_8, we want to copy our Axion model so that we can use it later:


```
cd MG5_aMC_v3_5_8
cp -r ../../SM_Axion_UFO models/.
```


Inside MG5_aMC_v3_5_8, run


```
./bin/mg5_aMC
```

This will bring you into the MG5 interface, where we will generate the interactions we want to inspect. We will want to use pythia, import our model, and look at jets with b quarks, so we need to set this up. Then we can generate the desired interaction and output it to a given directory for further analysis (you only have to do the install steps the first time):


```
install hepmc
install pythia8
import model SM_Axion_UFO
define j = j b b~
generate mu+ mu- > ax a, (ax > b b~)
output mu_mu_ax_gamma
exit
```

This will create a directory called **mu_mu_ax_gamma** inside your MG5 directory. Note that Madgraph uses "a" for photons, not to be confused with "ax" for ALPs. If you have MG5 locally, you can also look at the Feynman diagrams when inside the MG5 interface by running "display diagrams" before exiting.

Inside mu_mu_ax_gamma, you will see a directory called **Cards**. This holds the parameters for our model and collisions. There are two cards we want to pay special attentiont to: **run_card.dat** and **param_card.dat**. run_card.dat will determine number of events and all sorts of kinematic constraints, such as the beam energy and the minimum $p_T$ of the photon and jets. param_card.dat holds the masses and couplings of the particles. The "Ma" and "Wa" parameters hold the mass and decay width of the ALP, respectively. We will consider an effective coupling of $0.1$, for which here are some example decay widths for different masses:

<div align="center">
  <img width="417" alt="image" src="https://github.com/user-attachments/assets/76a2a623-2e9b-4740-a397-e1f53f05f1b2" />
</div>


<div align="center">
  <img src="https://github.com/user-attachments/assets/e906d220-c754-46dd-a8f8-d3f2389aa6ee" alt="image" />
</div>
<br>

For a further discussion on decay widths of ALPs, see D.1 of Bauer et al. (https://link.springer.com/article/10.1007/JHEP12(2017)044). Let's consider an ALP mass of 20 GeV (set Ma to 20 and Wa to 0.340122) at a beam energy of 1500GeV (3TeV CoM energy), and a photon $p_T$ (pta) of 50 GeV. Now we are ready to generate events inside our mu_mu_ax_gamma directory:


```
cp Cards/param_card.dat bin/internal/ufomodel/.
./bin/generate_events m20_3TeV_50GeV_gamma
```

You should see this sort of output:

```
The following switches determine which programs are run:
/=================== Description ===================|============= values ==============|======== other options ========\
| 1. Choose the shower/hadronization program        |        shower = OFF               |     Pythia8                   |
| 2. Choose the detector simulation program         |      detector = Not Avail.        |     Please install module     |
| 3. Choose an analysis package (plot/convert)      |      analysis = Not Avail.        |     Please install module     |
| 4. Decay onshell particles                        |       madspin = OFF               |     ON|onshell|full           |
| 5. Add weights to events for new hypp.            |      reweight = OFF               |     ON                        |
\=======================================================================================================================/
Either type the switch number (1 to 5) to change its setting,
Set any switch explicitly (e.g. type 'shower=Pythia8' at the prompt)
Type 'help' for the list of all valid option
Type '0', 'auto', 'done' or just press enter when you are done.
```

since we want to shower with pythia, we run

```
shower = Pythia8
```

and then "return" to launch. If your simulation crashes without any explanation when merging the pythia8 runs, it is likely that the pythia8 version defined in MG5 is different from the version defined in your environment. Make sure these are equivalent or that you don't have pythia8 separately in the environment.

When the runs finish, you should have a new directory called "Events" which holds another directory "m20_3TeV_50GeV_gamma", where you will find these files:

```
m20_3TeV_20GeV_gamma_tag_1_banner.txt  run_shower.sh  tag_1_djrs.dat  tag_1_pts.dat
tag_1_pythia8.cmd	tag_1_pythia8.log  tag_1_pythia8_events.hepmc.gz  unweighted_events.lhe.gz
```


The .txt file will hold some of the MG5 output. At the bottom of this file you will find the cross-section of your interaction. We will continue with the tag_1_pythia8_events.hepmc.gz file, which holds the showered data of our collisions.

We have now finished "nature's part of the job", the physics that takes place when we collide muons together and produce photons and ALPs, which decay and hadronize to produce jets. Now we want to know what nature looks like when we, as humans, look at it using a detector. We pass the .hepmc file to an emulater which "smears" the truth-level data in a way that mimics our detector. Only then can we compare simulation to experiment.







&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 

## Detector Emulation

The detector emulation has three steps:

*  simulating event particles passing through the detector (**sim**)
*  digitisation of the signal left by the particles (**digi**)
*  reconstructing the particle tracks from detector information (**reco**)


For everything with the detector steps, use the singularity environment. Set up the singularity shell to have all dependencies:

```
singularity shell docker://gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9
source /opt/setup_mucoll.sh
```


### simulation
For the simulation step, Monte Carlo particles are passed through the detector with GEANT4. We pass the .hepmc file created by Pythia8 in event generation to the detector. Make sure you ran and set up the singularity environment as before:

```
singularity shell docker://gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9
source /opt/setup_mucoll.sh
```


Then create a sim directory, in which you run

```
ddsim --steeringFile ../mucoll-benchmarks/simulation/ilcsoft/steer_baseline.py \
--inputFile ../tag_1_pythia8_events.hepmc \
--numberOfEvents 10 \
--outputFile output_sim.slcio
```

Make sure the first two lines poing to the correct steer and .hepmc files. You can inspect the output file using

```
anajob output_sim.slcio
```

### digitisation

Next is the digitisation step, which typically involves a minimum amount of energy to be considered a hit and smears the energy to a realistic detector resolution. Make a digi directory and run

```
k4run ../mucoll-benchmarks/digitisation/k4run/digi_steer.py \
--LcioEvent.Files ../sim/output_sim.slcio
```

Which takes the sim output file as an input.

### reconstruction

For reconstruction, first make sure your environment is really set up correctly:

```
env | grep ACTS_
```

This should give

```
ACTS_TGeoFile=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.3.1/actstracking-1.2.2-tjfu4av5xb6ivzyihvi2a3djbpnqx5nk/share/ACTSTracking/data/MuColl_v1.root
ACTS_MatFile=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.3.1/actstracking-1.2.2-tjfu4av5xb6ivzyihvi2a3djbpnqx5nk/share/ACTSTracking/data/material-maps.json
```

Then create a reco directory and copy the settings from the mucoll-benchmarks directory into it:

```
cp -a /home/odschnei/USMCC/mucoll-benchmarks/reconstruction/k4run/PandoraSettings ./
```

Now you can run the reconstruction step:

```
k4run ../mucoll-benchmarks/reconstruction/k4run/reco_steer.py \
    --LcioEvent.Files ../digi/output_digi.slcio \
    --MatFile ${ACTS_MatFile} \
    --TGeoFile ${ACTS_TGeoFile}
```

Which takes the digi output file as an input. You can again inspect this file using anajob:

```
anajob outpu_reco.slcio
```

This will show you a bunch of different collections, representing hits in different calorimeters. The most important are MCParticle, which contains truth-level data of the event, and PandoraPFOs, which is the reconstructed Particle Flow Objects. Here is an example output for one event:

```
RUN: -1         EVENT: 0           DETECTOR: MuColl_v1
---------------------------------------------------------------------------
COLLECTION NAME                    COLLECTION TYPE            # OF ELEMENTS
===========================================================================
AllTracks                          Track                                 81
ECalBarrelCollection               SimCalorimeterHit                  30042
ECalEndcapCollection               SimCalorimeterHit                    412
EcalBarrelCollectionDigi           CalorimeterHit                     23482
EcalBarrelCollectionRec            CalorimeterHit                     23482
EcalBarrelRelationsSimDigi         LCRelation                         23482
EcalBarrelRelationsSimRec          LCRelation                         23482
EcalEndcapCollectionDigi           CalorimeterHit                        78
EcalEndcapCollectionRec            CalorimeterHit                        78
EcalEndcapRelationsSimDigi         LCRelation                            78
EcalEndcapRelationsSimRec          LCRelation                            78
HCalBarrelCollection               SimCalorimeterHit                  36299
HCalEndcapCollection               SimCalorimeterHit                    396
HCalRingCollection                 SimCalorimeterHit                    203
HCalRingCollectionDigi             CalorimeterHit                        25
HCalRingCollectionRec              CalorimeterHit                        25
HCalRingRelationsSimDigi           LCRelation                            25
HCalRingRelationsSimRec            LCRelation                            25
HcalBarrelCollectionDigi           CalorimeterHit                      5364
HcalBarrelCollectionRec            CalorimeterHit                      5364
HcalBarrelRelationsSimDigi         LCRelation                          5364
HcalBarrelRelationsSimRec          LCRelation                          5364
HcalEndcapCollectionDigi           CalorimeterHit                        22
HcalEndcapCollectionRec            CalorimeterHit                        22
HcalEndcapRelationsSimDigi         LCRelation                            22
HcalEndcapRelationsSimRec          LCRelation                            22
ITBarrelHits                       TrackerHitPlane                       92
ITBarrelHitsRelations              LCRelation                            92
ITEndcapHits                       TrackerHitPlane                        0
ITEndcapHitsRelations              LCRelation                             0
InnerTrackerBarrelCollection       SimTrackerHit                        115
InnerTrackerEndcapCollection       SimTrackerHit                         31
JetOut                             ReconstructedParticle                  4
MCParticle                         MCParticle                          1307
MuonHits                           CalorimeterHit                         9
MuonHitsRelations                  LCRelation                             9
OTBarrelHits                       TrackerHitPlane                       93
OTBarrelHitsRelations              LCRelation                            93
OTEndcapHits                       TrackerHitPlane                        0
OTEndcapHitsRelations              LCRelation                             0
OuterTrackerBarrelCollection       SimTrackerHit                        231
OuterTrackerEndcapCollection       SimTrackerHit                         67
PandoraClusters                    Cluster                               37
PandoraPFOs                        ReconstructedParticle                 43
PandoraStartVertices               Vertex                                43
SeedTracks                         Track                                 81
SelectedPandoraPFOs                ReconstructedParticle                 31
SiTracks                           Track                                 24
VXDBarrelHits                      TrackerHitPlane                      183
VXDBarrelHitsRelations             LCRelation                           183
VXDEndcapHits                      TrackerHitPlane                       18
VXDEndcapHitsRelations             LCRelation                            18
VertexBarrelCollection             SimTrackerHit                        190
VertexEndcapCollection             SimTrackerHit                         18
YokeBarrelCollection               SimCalorimeterHit                      6
YokeEndcapCollection               SimCalorimeterHit                      3
---------------------------------------------------------------------------
```

Since there are many collections, these files can become large very quickly when generating many events. To cut out all collections except MCParticle and PandoraPFOs, see trimmer.py in the tools directory.


### Visualization

If you logged into HPCC using the "-X -Y" add-on, you can visualize your events using the output file from your reco step:


```
ced2go -d ${MUCOLL_GEO} output_reco.slcio
```

This will be slow and buffering due to the pipeline created to the HPCC, but will give you a good visualiztion of your events and the calorimeters involved.

Now you know how to generate events and reconstruct them using the detector for the muon collider. You will have noticed that this takes a considerable amount of time for only few events. The next section describes how to generate multiple thousand events for an analysis.


&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 




## Submitting Jobs

To submit jobs to the cluster and generate many events, use jobSubmission.py. Make sure it correctly points to the mucoll-benchmarks folder.










