# DLPNO-CCSD(T) High-Level Reference Calculations

## Overview

Domain-based Local Pair Natural Orbital Coupled Cluster calculations provide gold standard reference energies for quantum algorithm validation and accuracy assessment.

## Calculation Details

- **Method**: DLPNO-CCSD(T)
- **Basis set**: aug-cc-pVTZ
- **Solvation**: CPCM water
- **Geometries**: All 71 structures from M06-2X PES scans
- **Purpose**: Ultimate accuracy benchmark for quantum computing applications

## Systematic Coverage

### Complete Reaction Coordinate
- **71 calculations**: One for each PES scan geometry
- **Bond distances**: 1.5 Å to 5.0 Å (0.05 Å increments)
- **Consistent basis**: M06-2X geometries for all CCSD(T) calculations

### Organisation
Each calculation organised in separate folder containing:
- `structure.xyz`: Geometry from M06-2X PES scan
- `dlpno_calculation.inp`: CCSD(T) input file
- `dlpno_calculation.out`: Output files with high-level energies

## Quantum Computing Applications

### VQE Algorithm Validation
- **Gold standard targets**: Ultimate accuracy goals for quantum algorithms
- **Error assessment**: Quantify quantum algorithm performance vs. best classical methods
- **Convergence criteria**: Establish quantum computation accuracy thresholds

### Resource Estimation
- **Classical comparison**: Computational cost baseline for quantum advantage assessment
- **Accuracy benchmarks**: Target precision for quantum molecular simulation
- **Method validation**: Verify DFA performance against correlated wavefunction methods

## Computational Significance

DLPNO-CCSD(T) represents:
- **Highest practical accuracy**: Near-exact treatment of electron correlation
- **Systematic benchmark**: Consistent high-level reference across reaction coordinate
- **Quantum target**: Ultimate goal for quantum computing molecular simulation

## Repository Structure

### Included
- `input_template/`: Representative input file and structure
- `sample_calculations/`: 1-2 example complete calculations
- `extract_dlpno_energies.py`: Python script to extract all CCSD(T) energies

### Full Dataset
- **71 complete calculations** performed but not uploaded (identical structure to examples)
- **Energy extraction**: Use provided Python script to reproduce energy compilation
- **Reproduction instructions** using template files

## Data Extraction

Use the provided Python script to extract energies from your complete dataset:
```bash
python extract_dlpno_energies.py /path/to/your/71/folders/ --ccsd -o ccsd_energies.csv
