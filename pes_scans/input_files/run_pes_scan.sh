#!/bin/bash
#SBATCH --job-name=pes
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128g
#SBATCH --time=72:00:00
#SBATCH --partition=defq

# Load modules
module purge
module load orca-uoneasy/5.0.4-gompi-2022a-UCX-1.15.0

# Export paths
export ORCA=`which orca`

# Run ORCA
${ORCA} *.inp > orca.out
