# Import the necessary modules
import sys

# Define a function to extract the desired residues from the PDB file
def extract_residues(pdb_file, residues_to_extract):
    # Create a set of the desired residue IDs
    residue_ids = set(residues_to_extract)
    
    # Open the input PDB file
    with open(pdb_file, 'r') as f:
        # Loop through each line of the file
        for line in f:
            # Check if the line corresponds to a desired residue
            if line.startswith('ATOM') and line[17:26] in residue_ids:
                # If it is a desired residue, print the line to the output file
                print(line.rstrip())

# Define the input PDB file
pdb_file = 'input.pdb'

# Define the residues to extract
residues_to_extract = [
    'GLN A 213', 'ILE A 176', 'THR E 245', 'GLU D 294','CYS D 293','LEU D 278','PRO E  69','PHE E  71'
    # Add more residues as needed
]

# Define the output file
output_file = 'output.pdb'

# Call the function to extract the desired residues
extract_residues(pdb_file, residues_to_extract)
