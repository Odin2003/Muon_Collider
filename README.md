# Muon Collider
This roughly follows the tutorials found at https://mcd-wiki.web.cern.ch/software/tutorials/fermilab2024/ with event generation being done by MadGraph5 and Pythia. The .hepmc file produced through pythia is then inserted at the "Detector Simulation" step of the CERN 2023 tutorial. After the simulation part, the steps follow the Fermilab 2024 tutorial. All parts should be followed on the **HPCC**:

```
ssh -X -Y {USERNAME}@login.hpcc.ttu.edu
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
cd MG5_aMC_v3_5_8
```

Within MG5_aMC_v3_5_8, we want to copy our Axion model so that we can use it later:


```
cp -r ../SM_Axion_UFO models/.
```


Set up the singularity shell to have all dependencies:

```
singularity shell docker://gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9
source /opt/setup_mucoll.sh
```


Inside MG5_aMC_v3_5_8, run


```
./bin/mg5_aMC
```

This will bring you into the MG5 interface, where we will generate the interactions we want to inspect. We will want to use pythia, import our model, and look at jets with b quarks, so we need to set this up. Then we can generate the desired interaction and output it to a given directory for further analysis:


```
install pythia8
import model SM_Axion_UFO
define j = j b b~
generate mu+ mu- > ax a, (ax > b b~)
output mu_mu_ax_gamma
exit
```

This will create a directory called **mu_mu_ax_gamma** inside your MG5 directory. Note that Madgraph uses "a" for photons, not to be confused with "ax" for ALPs. If you have MG5 locally, you can also look at the Feynman diagrams when inside the MG5 interface by running "display diagrams" before exiting.

Inside mu_mu_ax_gamma, you will see a directory called **Cards**. This holds the parameters for our model and collisions. There are two cards we want to pay special attentiont to **run_card.dat** and **param_card.dat**. run_card.dat will determine number of events and all sorts of kinematic constraints, such as the beam energy and the minimum $p_T$ of the photon and jets. param_card.dat holds the masses and couplings of the particles. The "Ma" and "Wa" parameters hold the mass and decay width of the ALP, respectively. We will consider a coupling of $0.1$, for which here are some example decay widths for different masses:

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
./bin/generate events m20_3TeV_50GeV_gamma
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
m20_3TeV_20GeV_gamma_tag_1_banner.txt  run_shower.sh  tag_1_djrs.dat  tag_1_pts.dat  tag_1_pythia8.cmd	tag_1_pythia8.log  tag_1_pythia8_events.hepmc.gz  unweighted_events.lhe.gz
```


The .txt file will hold some of the MG5 output. At the bottom of this file you will find the cross-section of your interaction. We will continue with the tag_1_pythia8_events.hepmc.gz file, which holds the showered data of our collisions. This we will pass to the muon collider to see what our collisions look like inside that detector.












