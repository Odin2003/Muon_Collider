import os

current_dir = os.getcwd()
log_dir = os.path.join(current_dir, "log")
print("Current directory: ", current_dir)

# Define job parameters
njobs = 1000
nevents_per_job = 1
runnumber = 100
jobname_prefix = "mu_coll"

# Ensure log directory exists
if not os.path.exists(log_dir):
    print(f"Creating log directory: {log_dir}")
    os.makedirs(log_dir)

# Singularity command
singularity_cmd = "singularity exec docker://gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9 bash -c"

# Job scripts list
fnames = []
for i in range(njobs):
    jobname = f"{jobname_prefix}_{i}"
    
    # Modify simulation command with job-specific parameters
    sim_cmd_tmp = f"""
    mkdir -p sim
    cd sim
    ddsim --steeringFile ../mucoll-benchmarks/simulation/ilcsoft/steer_baseline.py \
          --inputFile ../tag_1_pythia8_events.hepmc \
          --numberOfEvents {nevents_per_job} \
          --outputFile output_sim_run{runnumber}_{i}.slcio
    cd ..
    """

    # Define digitization and reconstruction commands
    digi_cmd = f"""
    mkdir -p digi
    mkdir digi_{i}
    cd digi_{i}
    k4run ../mucoll-benchmarks/digitisation/k4run/digi_steer.py \
          --LcioEvent.Files ../sim/output_sim_run{runnumber}_{i}.slcio 
    mv output_digi.slcio ../digi/output_digi_run{runnumber}_{i}.slcio
    cd ..
    rm -r digi_{i}
    """

    reco_cmd = rf"""
    mkdir -p reco
    mkdir reco_{i}
    cd reco_{i}
    cp -a ../mucoll-benchmarks/reconstruction/k4run/PandoraSettings ./
    k4run ../mucoll-benchmarks/reconstruction/k4run/reco_steer.py \\
            --LcioEvent.Files ../digi/output_digi_run{runnumber}_{i}.slcio \\
            --MatFile \$MATFILE \\
            --TGeoFile \$TGEOFILE
    mv output_reco.slcio ../reco/output_reco_run{runnumber}_{i}.slcio
    cd ..
    rm -r reco_{i}
    """


    # SLURM job script
    submissiontext = rf"""#!/bin/bash
#SBATCH -J {jobname}
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o {log_dir}/{jobname}.%j.out
#SBATCH -e {log_dir}/{jobname}.%j.err
#SBATCH -p nocona

{singularity_cmd} "
    source /opt/setup_mucoll.sh
    export MATFILE=\$ACTS_MatFile
    export TGEOFILE=\$ACTS_TGeoFile
    {sim_cmd_tmp}
    {digi_cmd}
    {reco_cmd}
"
"""

    # Write the job submission script
    fname = f"{log_dir}/submit_{jobname}.sh"
    with open(fname, "w") as f:
        f.write(submissiontext)

    fnames.append(fname)

# Create a script to submit all jobs
submit_sh = os.path.join(current_dir, "submit_all.sh")
with open(submit_sh, "w") as f:
    f.write("#!/bin/bash\n")
    for fname in fnames:
        f.write(f"sbatch {fname}\n")

os.system(f"chmod +x {submit_sh}")

print(f"Submission script written to {submit_sh}")
print("To submit jobs, run:")
print(f"bash {submit_sh}")

