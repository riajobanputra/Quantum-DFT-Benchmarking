# PES Scan Results

## Energy Data Files

- **`energies_pes_scan_gas.dat`**: Complete energy dataset for gas phase calculations
- **`energies_pes_scan_solvent.dat`**: Complete energy dataset with CPCM water solvation

## Trajectory File

- **`pes_trajectory.trj`**: Complete 71-structure trajectory showing β-carbon-sulfur bond breaking/formation
  - Visualises the entire reaction coordinate
  - Can be opened in ChimeraX, VMD, PyMOL, or other molecular viewers
  - Shows smooth transition from reactant to product

## Data Coverage

- **71 bond distances**: 1.5-5.0 Å (0.05 Å increments)  
- **Multiple DFAs**: All density functional approximations studied
- **Consistent basis**: ma-def2-SVP throughout

## Quantum Computing Applications

This data enables:
- **VQE training**: Reference energies for quantum circuit optimization
- **Algorithm validation**: Classical benchmarks for quantum method assessment  
- **Resource estimation**: Molecular complexity analysis for quantum devices
- **Reaction visualisation**: Understanding quantum optimization landscapes

## Usage

The trajectory file provides the complete structural evolution for quantum algorithm development and can be used to extract specific geometries as needed for quantum circuit testing.
