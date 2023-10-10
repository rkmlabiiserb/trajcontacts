# trajcontacts

**A Package for Calculating Residue-Residue Contacts from MD Trajectories**

Currently, there are two modes for contact determination:

1. **Normal Contact Analysis (norm):** The presence of a contact between two residues in macromolecular systems, such as proteins and nucleic acids, is established when the minimum inter-residue heavy atom pair distance falls within a specified cutoff (4-5 Å) for a majority of the simulation time (e.g., 75% or more of snapshots). This program can be utilized to extract residue contacts from long MD simulation trajectories as well as PDB structures.

2. **Continuous Contact Analysis (cont):** As described in Botello-Smith et al., Journal of Chemical Theory and Computation 15.4 (2019): 2116-2126 and Westerlund et al., The Journal of Chemical Physics 153.14 (2020).

This is a command-line program for Linux systems and relies on the MDTraj simulation analysis package (https://www.mdtraj.org/). It uses `mdtraj.load()` for trajectory/topology inputs, and inter-atomic distances are calculated using `mdtraj.distance()`. For efficiency and to avoid memory-related errors, save the trajectories without unnecessary atoms (solvent/ions or hydrogen atoms) and divide the trajectory into multiple chunks, then write their names (or pathnames) in a file (for example, name that file 'traj.dat') - see below.

## Installation

You can install trajcontacts by running:

pip install trajcontacts

After installation, you can access detailed options by typing:

trajcontacts -h

For a simple usage example, running the following command:

trajcontacts -p topologyfile -f file_containing_names/paths_to_coordinate_files -n 10

will execute the program on 10 processors and extract contacts with a 4.5 Ångstrom cutoff. Both 'topologyfile' (specified in the command line) and 'coordinatefile' (in the file containing names of coordinate files) should be specified as the same for extracting contacts from a PDB file.

## Example

trajcontacts -p 3sn6.pdb -f traj.dat -n 10

where 'traj.dat' is a file with a single line containing '3sn6.pdb'.

**How to Cite:**

Please cite the following research when using trajcontacts:

Madhu, Midhun K., Kunal Shewani, and Rajesh K. Murarka. "Biased Signaling in Mutated Variants of β2-Adrenergic Receptor: Insights from Molecular Dynamics Simulations." bioRxiv (2023): 2023-09.

**Copyright:**

Copyright belongs to the Computational Biophysics and Soft Matter Group, IISER Bhopal. Visit our website: https://home.iiserb.ac.in/~rkm/.
