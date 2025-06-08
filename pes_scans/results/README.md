# PES Scan Results

## Energy Data Files

- **`energies_pes_scan_gas.dat`**: Complete energy dataset for gas phase calculations
- **`energies_pes_scan_solvent.dat`**: Complete energy dataset with CPCM water solvation

## Data Structure

Each `.dat` file contains systematic energy data across:
- **71 bond distances**: 1.5-5.0 Å (0.05 Å increments)  
- **Multiple DFAs**: All density functional approximations studied
- **Consistent basis**: ma-def2-SVP throughout

## Sample Structures

The `sample_structures/` folder contains representative geometries from the 71-point scans:
- Key points along the reaction coordinate
- Reactant, transition state, and product regions
- Examples for quantum circuit design and testing

## Full Dataset

Complete set of 71 geometries per method available separately due to repository size constraints. The sample structures provide sufficient examples for:
- Quantum algorithm development
- VQE circuit testing  
- Method validation studies

## Quantum Computing Applications

This data enables:
- **VQE training**: Reference energies for quantum circuit optimisation
- **Algorithm validation**: Classical benchmarks for quantum method assessment  
- **Resource estimation**: Molecular complexity analysis for quantum devices
- **Hybrid development**: Quantum-classical algorithm integration studies

## Data Format

Energy files formatted for direct use in quantum computing workflows and classical analysis pipelines.
