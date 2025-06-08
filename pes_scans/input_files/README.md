# PES Scan Input Files

## Template Files

These input files serve as templates for systematic PES scanning across multiple density functional approximations.

### Files Included

- **`pes_scan_gas.inp`**: Gas phase PES scan template
- **`pes_scan_solvent.inp`**: CPCM water solvation PES scan template  
- **`run_pes_scan.sh`**: Shell script for automated execution

## Scan Parameters

- **Bond coordinate**: β-carbon-sulfur distance
- **Range**: 1.5 Å to 5.0 Å
- **Step size**: 0.05 Å (71 total points)
- **Basis set**: ma-def2-SVP
- **Charge**: -1 e

## Usage

### Manual Execution
Replace the functional keyword in the template files to scan with different DFAs:
- ωB97X-D3(BJ), M06-2X, B3LYP±D3(BJ)
- TPSS, SCAN, PBE±D3(BJ), LDA
- HF

### Automated Execution
Use `run_pes_scan.sh` to systematically execute scans across all functionals and both environments (gas/solvent).

## Output
Each scan generates:
- 71 optimised geometries along the reaction coordinate
- Energy data for quantum algorithm benchmarking
- Transition state identification for quantum barrier calculations
