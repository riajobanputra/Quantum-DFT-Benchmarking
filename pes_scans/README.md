# Potential Energy Surface Scans

## Overview

Systematic PES scans modeling the breaking/formation of the β-carbon-sulfur bond across multiple density functional approximations.

## Calculation Details

- **Bond distance range**: 1.5 Å to 5.0 Å
- **Step size**: 0.05 Å
- **Total points**: 71 geometries per method
- **Environments**: Gas phase and aqueous solution (CPCM)
- **Basis set**: ma-def2-SVP

## Methods Studied

**Hybrid Functionals:**
- ωB97X-D3(BJ)
- M06-2X
- B3LYP (with/without D3(BJ))

**Meta-GGA/GGA:**
- TPSS, SCAN
- PBE (with/without D3(BJ))
- LDA

**Reference:**
- Hartree-Fock (HF)

## Files Structure

### input_files/
- `pes_scan_gas.inp`: Template for gas phase calculations
- `pes_scan_solvent.inp`: Template with CPCM water solvation
- `run_pes_scan.sh`: Shell script for systematic execution

### results/
- `energies_pes_scan_gas.dat`: Complete energy data for all methods (gas phase)
- `energies_pes_scan_solvent.dat`: Complete energy data for all methods (solvent)
- `sample_structures/`: Representative geometries from the 71-point scan
- Full set of 71 structures generated but not uploaded (available on request)

## Quantum Computing Applications

These PES scans provide:
- **Training data** for VQE algorithm development
- **Benchmark energies** for quantum-classical comparison
- **Reaction coordinate mapping** for quantum optimization landscapes
- **Transition state identification** for quantum barrier calculations
- **Solvation effects** for quantum environment simulation

## Reproduction

Use the template input files with systematic functional substitution to reproduce the complete benchmark study. The shell script automates the process across all 71 bond distances for both gas phase and solvated environments.
