# Sample DLPNO-CCSD(T) Calculations

## Representative Examples

This folder contains 1-2 complete example calculations from the 71-point CCSD(T) benchmark study, demonstrating the full calculation workflow and file organization.

## Folder Structure

Each calculation folder contains:
- **`structure.xyz`**: Geometry from M06-2X PES scan at specific Cβ–S distance
- **`dlpno_calculation.inp`**: Complete ORCA input file
- **`run_calculation.sh`**: Shell script for job submission and execution

## Sample Points

The examples represent:
- Different points along the reaction coordinate
- Typical calculation setup and execution
- Expected output format and energy extraction

## Energy Extraction Example

Extract CCSD(T) energies from these examples:
```bash
python ../../scripts/extract_energies.py . --ccsd -o sample_ccsd_energies.csv
