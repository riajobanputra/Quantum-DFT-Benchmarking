{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Italic;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red143\green144\blue150;\red255\green255\blue255;\red42\green44\blue51;
\red66\green147\blue62;\red147\green0\blue147;\red50\green94\blue238;\red167\green87\blue5;}
{\*\expandedcolortbl;;\cssrgb\c62745\c63137\c65490;\cssrgb\c100000\c100000\c100000;\cssrgb\c21961\c22745\c25882;
\cssrgb\c31373\c63137\c30980;\cssrgb\c65098\c14902\c64314;\cssrgb\c25098\c47059\c94902;\cssrgb\c71765\c41961\c392;}
\paperw11900\paperh16840\margl1440\margr1440\vieww15040\viewh13160\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\i\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #!/usr/bin/env python3
\f1\i0 \cf4 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 """\
\pard\pardeftab720\partightenfactor0
\cf4 \strokec4 Energy Extraction Script for ORCA Output Files\
\
Extracts final energies from ORCA .out files across multiple folders\
and compiles them into a structured dataset for quantum computing applications.\
\
Author: [Your Name]\
Usage: python extract_energies.py [input_directory] [output_file]\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 """\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \strokec6 import\cf4 \strokec4  os\
\cf6 \strokec6 import\cf4 \strokec4  re\
\cf6 \strokec6 import\cf4 \strokec4  argparse\
\cf6 \strokec6 import\cf4 \strokec4  pandas \cf6 \strokec6 as\cf4 \strokec4  pd\
\cf6 \strokec6 from\cf4 \strokec4  pathlib \cf6 \strokec6 import\cf4 \strokec4  Path\
\
\cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 extract_orca_energy\cf4 \strokec4 (file_path):\
    \cf5 \strokec5 """\
\pard\pardeftab720\partightenfactor0
\cf4 \strokec4     Extract final SCF energy from ORCA output file.\
    \
    Args:\
        file_path (str): Path to ORCA .out file\
        \
    Returns:\
        float: Final SCF energy in Hartrees, or None if not found\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5     """\cf4 \strokec4 \
    \cf6 \strokec6 try\cf4 \strokec4 :\
        \cf6 \strokec6 with\cf4 \strokec4  \cf5 \strokec5 open\cf4 \strokec4 (file_path, \cf5 \strokec5 'r'\cf4 \strokec4 ) \cf6 \strokec6 as\cf4 \strokec4  f:\
            content \cf7 \strokec7 =\cf4 \strokec4  f.read()\
            \
        
\f0\i \cf2 \strokec2 # Pattern for final SCF energy
\f1\i0 \cf4 \strokec4 \
        scf_pattern \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 r'FINAL SINGLE POINT ENERGY\\s+(-?\\d+\\.\\d+)'\cf4 \strokec4 \
        \cf6 \strokec6 match\cf4 \strokec4  \cf7 \strokec7 =\cf4 \strokec4  re.search(scf_pattern, content)\
        \
        \cf6 \strokec6 if\cf4 \strokec4  \cf6 \strokec6 match\cf4 \strokec4 :\
            \cf6 \strokec6 return\cf4 \strokec4  \cf5 \strokec5 float\cf4 \strokec4 (\cf6 \strokec6 match\cf4 \strokec4 .group(\cf8 \strokec8 1\cf4 \strokec4 ))\
        \cf6 \strokec6 else\cf4 \strokec4 :\
            
\f0\i \cf2 \strokec2 # Alternative pattern for optimization energies
\f1\i0 \cf4 \strokec4 \
            opt_pattern \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 r'The optimization did not converge but reached the maximum number of'\cf4 \strokec4 \
            \cf6 \strokec6 if\cf4 \strokec4  opt_pattern \cf6 \strokec6 in\cf4 \strokec4  content:\
                \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Warning: Optimization did not converge in \cf4 \strokec4 \{file_path\}\cf5 \strokec5 "\cf4 \strokec4 )\
            \cf6 \strokec6 return\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
            \
    \cf6 \strokec6 except\cf4 \strokec4  Exception \cf6 \strokec6 as\cf4 \strokec4  e:\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Error reading \cf4 \strokec4 \{file_path\}\cf5 \strokec5 : \cf4 \strokec4 \{e\}\cf5 \strokec5 "\cf4 \strokec4 )\
        \cf6 \strokec6 return\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 extract_ccsd_t_energy\cf4 \strokec4 (file_path):\
    \cf5 \strokec5 """\
\pard\pardeftab720\partightenfactor0
\cf4 \strokec4     Extract DLPNO-CCSD(T) energy from ORCA output file.\
    \
    Args:\
        file_path (str): Path to ORCA .out file\
        \
    Returns:\
        float: CCSD(T) energy in Hartrees, or None if not found\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5     """\cf4 \strokec4 \
    \cf6 \strokec6 try\cf4 \strokec4 :\
        \cf6 \strokec6 with\cf4 \strokec4  \cf5 \strokec5 open\cf4 \strokec4 (file_path, \cf5 \strokec5 'r'\cf4 \strokec4 ) \cf6 \strokec6 as\cf4 \strokec4  f:\
            content \cf7 \strokec7 =\cf4 \strokec4  f.read()\
            \
        
\f0\i \cf2 \strokec2 # Pattern for CCSD(T) energy
\f1\i0 \cf4 \strokec4 \
        ccsd_pattern \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 r'DLPNO-CCSD\\(T\\) ENERGY:\\s+(-?\\d+\\.\\d+)'\cf4 \strokec4 \
        \cf6 \strokec6 match\cf4 \strokec4  \cf7 \strokec7 =\cf4 \strokec4  re.search(ccsd_pattern, content)\
        \
        \cf6 \strokec6 if\cf4 \strokec4  \cf6 \strokec6 match\cf4 \strokec4 :\
            \cf6 \strokec6 return\cf4 \strokec4  \cf5 \strokec5 float\cf4 \strokec4 (\cf6 \strokec6 match\cf4 \strokec4 .group(\cf8 \strokec8 1\cf4 \strokec4 ))\
        \cf6 \strokec6 return\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
        \
    \cf6 \strokec6 except\cf4 \strokec4  Exception \cf6 \strokec6 as\cf4 \strokec4  e:\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Error reading CCSD(T) from \cf4 \strokec4 \{file_path\}\cf5 \strokec5 : \cf4 \strokec4 \{e\}\cf5 \strokec5 "\cf4 \strokec4 )\
        \cf6 \strokec6 return\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 extract_geometry_info\cf4 \strokec4 (xyz_file):\
    \cf5 \strokec5 """\
\pard\pardeftab720\partightenfactor0
\cf4 \strokec4     Extract bond distance from xyz file (assumes specific atom ordering).\
    \
    Args:\
        xyz_file (str): Path to .xyz file\
        \
    Returns:\
        float: Bond distance in Angstroms, or None if not found\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5     """\cf4 \strokec4 \
    \cf6 \strokec6 try\cf4 \strokec4 :\
        \cf6 \strokec6 with\cf4 \strokec4  \cf5 \strokec5 open\cf4 \strokec4 (xyz_file, \cf5 \strokec5 'r'\cf4 \strokec4 ) \cf6 \strokec6 as\cf4 \strokec4  f:\
            lines \cf7 \strokec7 =\cf4 \strokec4  f.readlines()\
            \
        
\f0\i \cf2 \strokec2 # Skip header lines and extract coordinates
\f1\i0 \cf4 \strokec4 \
        coords \cf7 \strokec7 =\cf4 \strokec4  []\
        \cf6 \strokec6 for\cf4 \strokec4  line \cf6 \strokec6 in\cf4 \strokec4  lines[\cf8 \strokec8 2\cf4 \strokec4 :]:  
\f0\i \cf2 \strokec2 # Skip atom count and comment
\f1\i0 \cf4 \strokec4 \
            \cf6 \strokec6 if\cf4 \strokec4  line.strip():\
                parts \cf7 \strokec7 =\cf4 \strokec4  line.strip().split()\
                \cf6 \strokec6 if\cf4 \strokec4  \cf5 \strokec5 len\cf4 \strokec4 (parts) \cf7 \strokec7 >=\cf4 \strokec4  \cf8 \strokec8 4\cf4 \strokec4 :\
                    coords.append([\cf5 \strokec5 float\cf4 \strokec4 (parts[\cf8 \strokec8 1\cf4 \strokec4 ]), \cf5 \strokec5 float\cf4 \strokec4 (parts[\cf8 \strokec8 2\cf4 \strokec4 ]), \cf5 \strokec5 float\cf4 \strokec4 (parts[\cf8 \strokec8 3\cf4 \strokec4 ])])\
        \
        
\f0\i \cf2 \strokec2 # Calculate specific bond distance (modify indices as needed)
\f1\i0 \cf4 \strokec4 \
        \cf6 \strokec6 if\cf4 \strokec4  \cf5 \strokec5 len\cf4 \strokec4 (coords) \cf7 \strokec7 >=\cf4 \strokec4  \cf8 \strokec8 2\cf4 \strokec4 :\
            
\f0\i \cf2 \strokec2 # Example: distance between atoms 0 and 1
\f1\i0 \cf4 \strokec4 \
            \cf6 \strokec6 import\cf4 \strokec4  numpy \cf6 \strokec6 as\cf4 \strokec4  np\
            dist \cf7 \strokec7 =\cf4 \strokec4  np.linalg.norm(np.array(coords[\cf8 \strokec8 0\cf4 \strokec4 ]) \cf7 \strokec7 -\cf4 \strokec4  np.array(coords[\cf8 \strokec8 1\cf4 \strokec4 ]))\
            \cf6 \strokec6 return\cf4 \strokec4  dist\
        \
        \cf6 \strokec6 return\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
        \
    \cf6 \strokec6 except\cf4 \strokec4  Exception \cf6 \strokec6 as\cf4 \strokec4  e:\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Error reading geometry from \cf4 \strokec4 \{xyz_file\}\cf5 \strokec5 : \cf4 \strokec4 \{e\}\cf5 \strokec5 "\cf4 \strokec4 )\
        \cf6 \strokec6 return\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 scan_directories\cf4 \strokec4 (base_dir, pattern\cf7 \strokec7 =\cf5 \strokec5 '*.out'\cf4 \strokec4 ):\
    \cf5 \strokec5 """\
\pard\pardeftab720\partightenfactor0
\cf4 \strokec4     Recursively scan directories for ORCA output files.\
    \
    Args:\
        base_dir (str): Base directory to search\
        pattern (str): File pattern to match\
        \
    Returns:\
        list: List of file paths matching pattern\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5     """\cf4 \strokec4 \
    base_path \cf7 \strokec7 =\cf4 \strokec4  Path(base_dir)\
    \cf6 \strokec6 return\cf4 \strokec4  \cf5 \strokec5 list\cf4 \strokec4 (base_path.rglob(pattern))\
\
\pard\pardeftab720\partightenfactor0
\cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 main\cf4 \strokec4 ():\
    parser \cf7 \strokec7 =\cf4 \strokec4  argparse.ArgumentParser(description\cf7 \strokec7 =\cf5 \strokec5 'Extract energies from ORCA output files'\cf4 \strokec4 )\
    parser.add_argument(\cf5 \strokec5 'input_dir'\cf4 \strokec4 , \cf5 \strokec5 help\cf7 \strokec7 =\cf5 \strokec5 'Input directory containing ORCA output files'\cf4 \strokec4 )\
    parser.add_argument(\cf5 \strokec5 '-o'\cf4 \strokec4 , \cf5 \strokec5 '--output'\cf4 \strokec4 , default\cf7 \strokec7 =\cf5 \strokec5 'extracted_energies.csv'\cf4 \strokec4 , \
                       \cf5 \strokec5 help\cf7 \strokec7 =\cf5 \strokec5 'Output CSV file (default: extracted_energies.csv)'\cf4 \strokec4 )\
    parser.add_argument(\cf5 \strokec5 '--ccsd'\cf4 \strokec4 , action\cf7 \strokec7 =\cf5 \strokec5 'store_true'\cf4 \strokec4 , \
                       \cf5 \strokec5 help\cf7 \strokec7 =\cf5 \strokec5 'Extract CCSD(T) energies instead of SCF'\cf4 \strokec4 )\
    parser.add_argument(\cf5 \strokec5 '--include-geometry'\cf4 \strokec4 , action\cf7 \strokec7 =\cf5 \strokec5 'store_true'\cf4 \strokec4 ,\
                       \cf5 \strokec5 help\cf7 \strokec7 =\cf5 \strokec5 'Include geometry information from xyz files'\cf4 \strokec4 )\
    \
    args \cf7 \strokec7 =\cf4 \strokec4  parser.parse_args()\
    \
    
\f0\i \cf2 \strokec2 # Find all output files
\f1\i0 \cf4 \strokec4 \
    out_files \cf7 \strokec7 =\cf4 \strokec4  scan_directories(args.input_dir, \cf5 \strokec5 '*.out'\cf4 \strokec4 )\
    \
    \cf6 \strokec6 if\cf4 \strokec4  \cf6 \strokec6 not\cf4 \strokec4  out_files:\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"No .out files found in \cf4 \strokec4 \{args.input_dir\}\cf5 \strokec5 "\cf4 \strokec4 )\
        \cf6 \strokec6 return\cf4 \strokec4 \
    \
    \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Found \cf4 \strokec4 \{\cf5 \strokec5 len\cf4 \strokec4 (out_files)\}\cf5 \strokec5  output files"\cf4 \strokec4 )\
    \
    
\f0\i \cf2 \strokec2 # Extract energies
\f1\i0 \cf4 \strokec4 \
    results \cf7 \strokec7 =\cf4 \strokec4  []\
    \cf6 \strokec6 for\cf4 \strokec4  out_file \cf6 \strokec6 in\cf4 \strokec4  out_files:\
        folder_name \cf7 \strokec7 =\cf4 \strokec4  out_file.parent.name\
        file_name \cf7 \strokec7 =\cf4 \strokec4  out_file.name\
        \
        
\f0\i \cf2 \strokec2 # Extract energy
\f1\i0 \cf4 \strokec4 \
        \cf6 \strokec6 if\cf4 \strokec4  args.ccsd:\
            energy \cf7 \strokec7 =\cf4 \strokec4  extract_ccsd_t_energy(out_file)\
            energy_type \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 'CCSD(T)'\cf4 \strokec4 \
        \cf6 \strokec6 else\cf4 \strokec4 :\
            energy \cf7 \strokec7 =\cf4 \strokec4  extract_orca_energy(out_file)\
            energy_type \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 'SCF'\cf4 \strokec4 \
        \
        
\f0\i \cf2 \strokec2 # Extract geometry info if requested
\f1\i0 \cf4 \strokec4 \
        bond_distance \cf7 \strokec7 =\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 \
        \cf6 \strokec6 if\cf4 \strokec4  args.include_geometry:\
            xyz_files \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 list\cf4 \strokec4 (out_file.parent.glob(\cf5 \strokec5 '*.xyz'\cf4 \strokec4 ))\
            \cf6 \strokec6 if\cf4 \strokec4  xyz_files:\
                bond_distance \cf7 \strokec7 =\cf4 \strokec4  extract_geometry_info(xyz_files[\cf8 \strokec8 0\cf4 \strokec4 ])\
        \
        result \cf7 \strokec7 =\cf4 \strokec4  \{\
            \cf5 \strokec5 'folder'\cf4 \strokec4 : folder_name,\
            \cf5 \strokec5 'file'\cf4 \strokec4 : file_name,\
            \cf5 \strokec5 'energy_hartree'\cf4 \strokec4 : energy,\
            \cf5 \strokec5 'energy_type'\cf4 \strokec4 : energy_type\
        \}\
        \
        \cf6 \strokec6 if\cf4 \strokec4  args.include_geometry \cf6 \strokec6 and\cf4 \strokec4  bond_distance \cf6 \strokec6 is\cf4 \strokec4  \cf6 \strokec6 not\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 :\
            result[\cf5 \strokec5 'bond_distance_angstrom'\cf4 \strokec4 ] \cf7 \strokec7 =\cf4 \strokec4  bond_distance\
        \
        results.append(result)\
        \
        \cf6 \strokec6 if\cf4 \strokec4  energy \cf6 \strokec6 is\cf4 \strokec4  \cf6 \strokec6 not\cf4 \strokec4  \cf8 \strokec8 None\cf4 \strokec4 :\
            \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"\uc0\u10003  \cf4 \strokec4 \{folder_name\}\cf5 \strokec5 /\cf4 \strokec4 \{file_name\}\cf5 \strokec5 : \cf4 \strokec4 \{energy:.8f\}\cf5 \strokec5  Hartree"\cf4 \strokec4 )\
        \cf6 \strokec6 else\cf4 \strokec4 :\
            \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"\uc0\u10007  \cf4 \strokec4 \{folder_name\}\cf5 \strokec5 /\cf4 \strokec4 \{file_name\}\cf5 \strokec5 : Energy not found"\cf4 \strokec4 )\
    \
    
\f0\i \cf2 \strokec2 # Convert to DataFrame and save
\f1\i0 \cf4 \strokec4 \
    df \cf7 \strokec7 =\cf4 \strokec4  pd.DataFrame(results)\
    \
    
\f0\i \cf2 \strokec2 # Sort by folder name (useful for numerical ordering)
\f1\i0 \cf4 \strokec4 \
    df \cf7 \strokec7 =\cf4 \strokec4  df.sort_values(\cf5 \strokec5 'folder'\cf4 \strokec4 )\
    \
    
\f0\i \cf2 \strokec2 # Add energy in other units
\f1\i0 \cf4 \strokec4 \
    df[\cf5 \strokec5 'energy_ev'\cf4 \strokec4 ] \cf7 \strokec7 =\cf4 \strokec4  df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ] \cf7 \strokec7 *\cf4 \strokec4  \cf8 \strokec8 27.2114\cf4 \strokec4   
\f0\i \cf2 \strokec2 # Hartree to eV
\f1\i0 \cf4 \strokec4 \
    df[\cf5 \strokec5 'energy_kcal_mol'\cf4 \strokec4 ] \cf7 \strokec7 =\cf4 \strokec4  df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ] \cf7 \strokec7 *\cf4 \strokec4  \cf8 \strokec8 627.509\cf4 \strokec4   
\f0\i \cf2 \strokec2 # Hartree to kcal/mol
\f1\i0 \cf4 \strokec4 \
    \
    
\f0\i \cf2 \strokec2 # Save results
\f1\i0 \cf4 \strokec4 \
    df.to_csv(args.output, index\cf7 \strokec7 =\cf8 \strokec8 False\cf4 \strokec4 )\
    \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"\\nResults saved to \cf4 \strokec4 \{args.output\}\cf5 \strokec5 "\cf4 \strokec4 )\
    \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Successfully extracted \cf4 \strokec4 \{df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].notna().\cf5 \strokec5 sum\cf4 \strokec4 ()\}\cf5 \strokec5  energies"\cf4 \strokec4 )\
    \
    
\f0\i \cf2 \strokec2 # Display summary statistics
\f1\i0 \cf4 \strokec4 \
    \cf6 \strokec6 if\cf4 \strokec4  \cf6 \strokec6 not\cf4 \strokec4  df.empty \cf6 \strokec6 and\cf4 \strokec4  df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].notna().\cf5 \strokec5 any\cf4 \strokec4 ():\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"\\nEnergy Statistics (\cf4 \strokec4 \{energy_type\}\cf5 \strokec5 ):"\cf4 \strokec4 )\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Mean: \cf4 \strokec4 \{df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].mean():.6f\}\cf5 \strokec5  Hartree"\cf4 \strokec4 )\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Range: \cf4 \strokec4 \{df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].\cf5 \strokec5 min\cf4 \strokec4 ():.6f\}\cf5 \strokec5  to \cf4 \strokec4 \{df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].\cf5 \strokec5 max\cf4 \strokec4 ():.6f\}\cf5 \strokec5  Hartree"\cf4 \strokec4 )\
        \cf6 \strokec6 print\cf4 \strokec4 (\cf5 \strokec5 f"Span: \cf4 \strokec4 \{(df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].\cf5 \strokec5 max\cf4 \strokec4 () \cf7 \strokec7 -\cf4 \strokec4  df[\cf5 \strokec5 'energy_hartree'\cf4 \strokec4 ].\cf5 \strokec5 min\cf4 \strokec4 ()) \cf7 \strokec7 *\cf4 \strokec4  \cf8 \strokec8 627.509\cf4 \strokec4 :.2f\}\cf5 \strokec5  kcal/mol"\cf4 \strokec4 )\
\
\cf6 \strokec6 if\cf4 \strokec4  __name__ \cf7 \strokec7 ==\cf4 \strokec4  \cf5 \strokec5 "__main__"\cf4 \strokec4 :\
    main()}