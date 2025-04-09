#!/bin/bash

# Set the number of events, default to 10 if not provided
n_events=${1:-10}

# Step 1: Create sim directory and run ddsim
mkdir -p sim
cd sim || exit
if [[ ! -f output_sim.slcio ]]; then
    echo "Running ddsim..."
    ddsim --steeringFile /scratch/odschnei/mumu_ax_gamma/mucoll-benchmarks/simulation/ilcsoft/steer_baseline.py \
          --inputFile ../tag_1_pythia8_events.hepmc \
          --numberOfEvents "$n_events" \
          --outputFile output_sim.slcio
else
    echo "Simulation already completed. Skipping ddsim."
fi
cd ..

# Step 2: Create digi directory and run digitization
mkdir -p digi
cd digi || exit
if [[ ! -f output_digi.slcio ]]; then
    echo "Running digitization..."
    k4run /scratch/odschnei/mumu_ax_gamma/mucoll-benchmarks/digitisation/k4run/digi_steer.py \
          --LcioEvent.Files ../sim/output_sim.slcio
else
    echo "Digitization already completed. Skipping k4run for digitization."
fi
cd ..

# Step 3: Create reco directory, copy PandoraSettings, and run reconstruction
mkdir -p reco
cd reco || exit
if [[ ! -f output_reco.slcio ]]; then
    echo "Running reconstruction..."
    rm -rf PandoraSettings
    cp -a /scratch/odschnei/mumu_ax_gamma/mucoll-benchmarks/reconstruction/k4run/PandoraSettings ./

    k4run /scratch/odschnei/mumu_ax_gamma/mucoll-benchmarks/reconstruction/k4run/reco_steer.py \
          --LcioEvent.Files ../digi/output_digi.slcio \
          --MatFile "${ACTS_MatFile}" \
          --TGeoFile "${ACTS_TGeoFile}"
else
    echo "Reconstruction already completed. Skipping k4run for reconstruction."
fi

# Workflow complete
echo "Workflow completed successfully."
