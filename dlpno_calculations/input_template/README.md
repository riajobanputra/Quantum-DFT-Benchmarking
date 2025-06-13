# DLPNO-CCSD(T) Input Template

## Template Files

- **`dlpno_template.inp`**: Standard DLPNO-CCSD(T) input file template
- **`structure_template.xyz`**: Example geometry from M06-2X PES scan

## Input File Structure

The template demonstrates the complete ORCA input setup for high-level reference calculations:

### Key Settings
- **Method**: DLPNO-CCSD(T)
- **Basis set**: aug-cc-pVTZ
- **Solvation**: CPCM water model
- **Charge**: -1 e
- **Memory**: Optimised for large basis calculations

### Critical Parameters
- DLPNO thresholds for accuracy/efficiency balance
- Proper auxiliary basis sets for correlation treatment
- Convergence criteria for coupled cluster iterations

## Usage

### Single Calculation
Replace the geometry in the template with your target structure and execute:
```bash
orca dlpno_template.inp > dlpno_calculation.out
