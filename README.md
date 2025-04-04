# Muon Collider
This roughly follows the tutorials found at https://mcd-wiki.web.cern.ch/software/tutorials/fermilab2024/ with event generation being done by MadGraph5 and Pythia. The .hepmc file produced through pythia is then inserted at the "Detector Simulation" step of the CERN 2023 tutorial. After the simulation part, the steps follow the Fermilab 2024 tutorial. All parts should be followed on the **HPCC**.



## Event Generation
### MadGraph 5
Generating events is done with MadGraph5. Here I will describe the process to generate events for muon collisions in which an Axion-Like Particle (ALP) and a photon are produced. The ALP consequently decays to $b ~ \bar{b}$ quarks:

<img width="200" alt="image" src="https://github.com/user-attachments/assets/e2531751-7770-47f1-a42e-499d2eeeca67" />


Create a software folder and inside download the MadGraph software from https://launchpad.net/mg5amcnlo :

```
mkdir software
cd software
wget https://launchpad.net/mg5amcnlo/3.0/3.6.x/+download/MG5_aMC_v3.5.8.tar.gz
tar -xvf MG5_aMC_v3.5.8.tar.gz
```

Set up the singularity shell to have all dependencies:

```
singularity shell docker://gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9
source /opt/setup_mucoll.sh
```


Inside MG5_aMC_v3.5.8, run


```
./bin/mg5_aMC
```

This will bring you into the MG5 interface. This is where we will generate the interactions we want to inspect.















