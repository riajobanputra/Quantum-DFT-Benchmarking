# Quantum-DFT-Benchmarking
A comprehensive density functional theory (DFT) study of β-carbon-sulfur bond breaking in CDK12 inhibitor mechanisms, providing classical reference data for quantum algorithm development.

## Overview
This repository contains DFT calculations that serve as benchmarks for quantum computing algorithms, particularly Variational Quantum Eigensolver (VQE) development. The study focuses on the **thio-Michael addition mechanism** - a fundamental covalent bond formation process that represents an ideal test case for quantum advantage demonstrations in molecular simulation.

## Chemical Context
Novel small-molecule inhibitors of CDK12 have shown promise in treating myotonic dystrophy type 1 (DM1) through covalent bond formation with cysteine 1039 in the CDK12 active site. The selectivity of these inhibitors relies on the **thio-Michael addition mechanism** - specifically the nucleophilic attack at the β-carbon leading to Cβ–S bond formation. Understanding this rate-determining step is critical for optimising inhibitor design and represents a challenging quantum mechanical process ideal for quantum computing applications.
The nucleophilic addition of thiolates to Michael acceptors has been previously investigated computationally. To gain fundamental understanding of this reaction mechanism, comprehensive quantum mechanical methods were employed to establish a reliable basis for future quantum algorithm development and validation.

## Computational Methodology
Kohn–Sham density functional theory calculations were performed using version 5.0.4 of the ORCA software package on the chemically active region of interest. Several density-functional approximations (DFAs) were chosen, including ωB97X-D3(BJ), M06-2X, LDA, TPSS, and SCAN, as well as B3LYP and PBE, both with and without the D3(BJ) dispersion correction. Additionally, Hartree-Fock (HF), a wavefunction-based method, was included.
All calculations were performed with the ma-def2-SVP basis set and a charge of–1 e. Potential energy surface (PES) scans were performed for each DFA in the gas phase to model the breaking of the β-carbon-sulfur (Cβ–S) bond. These scans involved scanning the Cβ-S bond distance from 1.5 Å to 5.0 Å with a step size of 0.05 Å. This was repeated in a continuum solvent of water using the conductor-like polarisable continuum model (CPCM).
Structures identified from the PES scans were optimised using M06-2X, which, among the DFAs employed, provided the most well-defined transition state peak for the Cβ-S bond breaking and represented the highest level of theory to yield a clear transition state. Geometry optimisations were performed on the lowest energy structure identified from the M06-2X PES scan to confirm the reactant minimum. Transition state optimisations were performed on the highest energy structure also identified from the M06-2X PES scan, specifically optimising to a first-order saddle point to locate the transition state. The single-point energy and Gibbs free energy were extracted from these optimisations. Vibrational frequency analysis of the optimised reactant minimum confirmed the absence of imaginary frequencies, indicating a true energy minimum. For the optimised transition state, the same analysis revealed a single imaginary frequency, characteristic of a transition state and corresponding to the Cβ-S bond breaking.
The resulting M06-2X optimised structures (reactant and transition state) were then used as starting geometries for geometry optimisations with the remaining DFAs to ensure that each converged to its own local minimum and transition state structure on their respective PES. The single-point energy and Gibbs free energy values were subsequently extracted for all DFAs at their converged optimised geometries.
DLPNO-CCSD(T) single-point energy calculations were conducted on each M06-2X optimised geometry obtained from the PES scans using the aug-cc-pVTZ basis set with implicit solvation in water, using CPCM. The M06-2X geometries used for the DLPNO-CCSD(T) calculations provides a consistent structural basis for comparing the single-point energies obtained from this higher-level method across the reaction coordinate.

## Quantum Computing Applications
This systematic DFT study of covalent drug binding mechanisms provides:
- Classical reference energies for VQE algorithm validation
- Benchmark data for quantum advantage demonstrations in drug discovery
- Resource estimation for near-term quantum devices (~12-16 qubits)
- Test cases for quantum-classical hybrid algorithms in pharmaceutical applications

## Repository Structure
```
├── input_files/     # ORCA calculation inputs
├── results/         # DFT energies and geometries
└── scripts/         # Analysis tools
```

## Usage
The calculation results serve as validation targets for quantum algorithms studying covalent bond formation mechanisms in drug discovery - a fundamental quantum mechanical process ideal for demonstrating quantum computational advantages in pharmaceutical research.
