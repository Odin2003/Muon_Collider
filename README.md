# Muon Collider
This roughly follows the tutorials found at https://mcd-wiki.web.cern.ch/software/tutorials/fermilab2024/ with event generation being done by MadGraph5 and Pythia. The .hepmc file produced through pythia is then inserted at the "Detector Simulation" step of the CERN 2023 tutorial. After the simulation part, the steps follow the Fermilab 2024 tutorial.

## Event Generation
### MadGraph 5
Generating events is done with MadGraph5. Here I will describe the process to generate events for muon collisions in which an Axion-Like Particle (ALP) and a photon are produced. The ALP consequently decays to $ b ~ \bar{b} $ quarks.
