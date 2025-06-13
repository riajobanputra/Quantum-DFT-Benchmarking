#!/usr/bin/env python3
"""
Energy Extraction Script for ORCA Output Files

Extracts final energies from ORCA .out files across multiple folders
and compiles them into a structured dataset for quantum computing applications.

Author: [Your Name]
Usage: python extract_energies.py [input_directory] [output_file]
"""

import os
import re
import argparse
import pandas as pd
from pathlib import Path

def extract_orca_energy(file_path):
    """
    Extract final SCF energy from ORCA output file.
    
    Args:
        file_path (str): Path to ORCA .out file
        
    Returns:
        float: Final SCF energy in Hartrees, or None if not found
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Pattern for final SCF energy
        scf_pattern = r'FINAL SINGLE POINT ENERGY\s+(-?\d+\.\d+)'
        match = re.search(scf_pattern, content)
        
        if match:
            return float(match.group(1))
        else:
            # Alternative pattern for optimization energies
            opt_pattern = r'The optimization did not converge but reached the maximum number of'
            if opt_pattern in content:
                print(f"Warning: Optimization did not converge in {file_path}")
            return None
            
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def extract_ccsd_t_energy(file_path):
    """
    Extract DLPNO-CCSD(T) energy from ORCA output file.
    
    Args:
        file_path (str): Path to ORCA .out file
        
    Returns:
        float: CCSD(T) energy in Hartrees, or None if not found
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Pattern for CCSD(T) energy
        ccsd_pattern = r'DLPNO-CCSD\(T\) ENERGY:\s+(-?\d+\.\d+)'
        match = re.search(ccsd_pattern, content)
        
        if match:
            return float(match.group(1))
        return None
        
    except Exception as e:
        print(f"Error reading CCSD(T) from {file_path}: {e}")
        return None

def extract_geometry_info(xyz_file):
    """
    Extract bond distance from xyz file (assumes specific atom ordering).
    
    Args:
        xyz_file (str): Path to .xyz file
        
    Returns:
        float: Bond distance in Angstroms, or None if not found
    """
    try:
        with open(xyz_file, 'r') as f:
            lines = f.readlines()
            
        # Skip header lines and extract coordinates
        coords = []
        for line in lines[2:]:  # Skip atom count and comment
            if line.strip():
                parts = line.strip().split()
                if len(parts) >= 4:
                    coords.append([float(parts[1]), float(parts[2]), float(parts[3])])
        
        # Calculate specific bond distance (modify indices as needed)
        if len(coords) >= 2:
            # Example: distance between atoms 0 and 1
            import numpy as np
            dist = np.linalg.norm(np.array(coords[0]) - np.array(coords[1]))
            return dist
        
        return None
        
    except Exception as e:
        print(f"Error reading geometry from {xyz_file}: {e}")
        return None

def scan_directories(base_dir, pattern='*.out'):
    """
    Recursively scan directories for ORCA output files.
    
    Args:
        base_dir (str): Base directory to search
        pattern (str): File pattern to match
        
    Returns:
        list: List of file paths matching pattern
    """
    base_path = Path(base_dir)
    return list(base_path.rglob(pattern))

def main():
    parser = argparse.ArgumentParser(description='Extract energies from ORCA output files')
    parser.add_argument('input_dir', help='Input directory containing ORCA output files')
    parser.add_argument('-o', '--output', default='extracted_energies.csv', 
                       help='Output CSV file (default: extracted_energies.csv)')
    parser.add_argument('--ccsd', action='store_true', 
                       help='Extract CCSD(T) energies instead of SCF')
    parser.add_argument('--include-geometry', action='store_true',
                       help='Include geometry information from xyz files')
    
    args = parser.parse_args()
    
    # Find all output files
    out_files = scan_directories(args.input_dir, '*.out')
    
    if not out_files:
        print(f"No .out files found in {args.input_dir}")
        return
    
    print(f"Found {len(out_files)} output files")
    
    # Extract energies
    results = []
    for out_file in out_files:
        folder_name = out_file.parent.name
        file_name = out_file.name
        
        # Extract energy
        if args.ccsd:
            energy = extract_ccsd_t_energy(out_file)
            energy_type = 'CCSD(T)'
        else:
            energy = extract_orca_energy(out_file)
            energy_type = 'SCF'
        
        # Extract geometry info if requested
        bond_distance = None
        if args.include_geometry:
            xyz_files = list(out_file.parent.glob('*.xyz'))
            if xyz_files:
                bond_distance = extract_geometry_info(xyz_files[0])
        
        result = {
            'folder': folder_name,
            'file': file_name,
            'energy_hartree': energy,
            'energy_type': energy_type
        }
        
        if args.include_geometry and bond_distance is not None:
            result['bond_distance_angstrom'] = bond_distance
        
        results.append(result)
        
        if energy is not None:
            print(f"✓ {folder_name}/{file_name}: {energy:.8f} Hartree")
        else:
            print(f"✗ {folder_name}/{file_name}: Energy not found")
    
    # Convert to DataFrame and save
    df = pd.DataFrame(results)
    
    # Sort by folder name (useful for numerical ordering)
    df = df.sort_values('folder')
    
    # Add energy in other units
    df['energy_ev'] = df['energy_hartree'] * 27.2114  # Hartree to eV
    df['energy_kcal_mol'] = df['energy_hartree'] * 627.509  # Hartree to kcal/mol
    
    # Save results
    df.to_csv(args.output, index=False)
    print(f"\nResults saved to {args.output}")
    print(f"Successfully extracted {df['energy_hartree'].notna().sum()} energies")
    
    # Display summary statistics
    if not df.empty and df['energy_hartree'].notna().any():
        print(f"\nEnergy Statistics ({energy_type}):")
        print(f"Mean: {df['energy_hartree'].mean():.6f} Hartree")
        print(f"Range: {df['energy_hartree'].min():.6f} to {df['energy_hartree'].max():.6f} Hartree")
        print(f"Span: {(df['energy_hartree'].max() - df['energy_hartree'].min()) * 627.509:.2f} kcal/mol")

if __name__ == "__main__":
    main()