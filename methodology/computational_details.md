# Computational Details

## Overview

Comprehensive quantum-classical benchmarking study of β-carbon-sulfur bond formation in CDK12 inhibitor mechanisms. Provides systematic DFT validation data for quantum computing algorithm development, particularly Variational Quantum Eigensolver (VQE) applications.

## System Definition

- **Chemical process**: Thio-Michael addition mechanism (covalent drug binding)
- **QM region**: CDK12 inhibitor + cysteine 1039 interaction site
- **System charge**: -1 e
- **Target bond**: β-carbon-sulfur formation/breaking
- **Quantum relevance**: Fundamental covalent bond process ideal for 12-16 qubit quantum circuits

## Computational Protocol

### Software and Setup
- **Package**: ORCA 5.0.4
- **Basis set**: ma-def2-SVP (quantum-classical mapping compatible)
- **Environments**: Gas phase and CPCM water solvation

### Methodology Hierarchy

#### 1. Potential Energy Surface Mapping
- **Scan range**: β-carbon-sulfur bond distance 1.5-5.0 Å (0.05 Å steps)
- **Total points**: 71 geometries per method
- **Methods**: 8+ density functional approximations + Hartree-Fock
- **Purpose**: Generate quantum algorithm training data

#### 2. Structure Optimization
- **Primary method**: M06-2X (clearest transition state definition)
- **Targets**: Reactant minimum and transition state
- **Validation**: Frequency analysis (0/1 imaginary frequencies)
- **Cross-validation**: All DFAs optimized from M06-2X starting geometries

#### 3. High-Level Reference
- **Method**: DLPNO-CCSD(T)/aug-cc-pVTZ
- **Scope**: All 71 PES geometries
- **Purpose**: Gold standard for quantum algorithm accuracy assessment

## Density Functional Approximations

**Systematic benchmark across accuracy levels:**

- **Hybrid**: ωB97X-D3(BJ), M06-2X, B3LYP ± D3(BJ)
- **Meta-GGA**: TPSS, SCAN  
- **GGA**: PBE ± D3(BJ)
- **LDA**: Local density approximation
- **Reference**: Hartree-Fock, DLPNO-CCSD(T)

## Quantum Computing Applications

### Algorithm Development
- **VQE validation**: Classical reference energies for quantum circuit optimization
- **Resource estimation**: Molecular complexity for near-term quantum devices
- **Quantum advantage**: Performance benchmarking against classical methods

### Target Applications
- **Transition state chemistry**: Quantum optimization landscape studies
- **Covalent drug design**: Quantum-enhanced pharmaceutical discovery
- **Hybrid algorithms**: Quantum-classical molecular simulation integration

## Data Organisation

Calculations systematically organized to support quantum algorithm development:
- **Reproducible templates**: Standard input files for method comparison
- **Benchmark datasets**: Energy surfaces for VQE training and validation  
- **Reference standards**: CCSD(T) accuracy targets for quantum computing goals

## Expected Impact

Foundation for quantum molecular simulation algorithm development, enabling:
- VQE circuit design and optimization
- Quantum advantage assessment in chemical applications
- Hybrid quantum-classical drug discovery methodologies

---

*Detailed implementation specifics available in individual folder README files.*
