# Import the necessary modules
import sys

# Define a function to extract the desired residues from the PDB file
def extract_residues(pdb_file, residues_to_extract, output_file):
    # Create a set of the desired residue IDs
    residue_ids = set(residues_to_extract)
    
    # Open the output file for writing
    with open(output_file, 'w') as out_file:
        # Open the input PDB file
        with open(pdb_file, 'r') as in_file:
            # Loop through each line of the file
            for line in in_file:
                # Check if the line corresponds to a desired residue
                if line.startswith('ATOM') and line[17:27].strip() in residue_ids:
                    # If it is a desired residue, write the line to the output file
                    out_file.write(line)

# Define the input PDB file
pdb_file = input("Enter the input PDB file name: ")

# Define the residues to extract
residues_to_extract = []
num_residues = int(input("Enter the number of residues to extract: "))
for i in range(num_residues):
    residue = input(f"Enter the residue {i+1} (GLN A 213): ")
    residues_to_extract.append(residue.strip())

# Define the output file
output_file = input("Enter the output PDB file name: ")

# Call the function to extract the desired residues and save them to the output file
extract_residues(pdb_file, residues_to_extract, output_file)

print("Done!")
