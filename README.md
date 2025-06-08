# Quantum-DFT-Benchmarking
A comprehensive density functional theory (DFT) study of β-carbon-sulfur bond breaking in CDK12 inhibitor mechanisms, providing classical reference data for quantum algorithm development.

## Overview
This repository contains DFT calculations that serve as benchmarks for quantum computing algorithms, particularly Variational Quantum Eigensolver (VQE) development. The study focuses on the **thio-Michael addition mechanism** - a fundamental covalent bond formation process that represents an ideal test case for quantum advantage demonstrations in molecular simulation.

## Chemical Context
This study focuses on the **thio-Michael addition mechanism** - the covalent bond formation between CDK12 inhibitors and cysteine 1039. The nucleophilic attack leading to Cβ–S bond formation represents a fundamental quantum mechanical process ideal for quantum computing applications and algorithm validation.

## Computational Methodology
Kohn–Sham density functional theory calculations were performed using ORCA 5.0.4 with multiple density-functional approximations: ωB97X-D3(BJ), M06-2X, LDA, TPSS, SCAN, B3LYP, and PBE (with/without D3(BJ) dispersion correction), plus Hartree-Fock. All calculations used the ma-def2-SVP basis set with -1e charge.

Potential energy surface scans modeled Cβ–S bond breaking from 1.5-5.0 Å (0.05 Å steps) in gas phase and water (CPCM). M06-2X provided the clearest transition state and was used for geometry optimizations of reactant minima and transition states. Frequency analysis confirmed proper stationary points (zero/one imaginary frequency for minima/transition states).

All DFAs were then optimized using M06-2X geometries as starting points. DLPNO-CCSD(T) single-point calculations with aug-cc-pVTZ basis set provided high-level reference energies for all structures.

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
