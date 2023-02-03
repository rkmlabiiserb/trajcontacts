# trajcontacts
A package to caculate residue-residue contacts from MD trajectories
The presence of a contact between two residues in macromolecular systems, such as proteins and nucleic acids, is established when the minimum interresidue heavy atom pair distance falls within a specified cutoff (4-5 Å) for a given majority (for example, 75% or above snapshots) of the simulation time. This program can be untilized for extracting residue contacts from long MD simulation trajectories as well as PDB structures.

This is a command line program for linux systems and depends on MDTraj simulation analysis package (https://www.mdtraj.org/): mdtraj.load() is used for trajectory/topology inputs and inter-atomic distances are calculated using mdtraj.distance().

After installation, type 'trajcontacts -h' for detailed options.

A simple 'trajcontacts -p topologyfile -f coordinatefile -n 10' will run the program on 10 processors and extract contacts with 4.5 angstrom cutoff. Both 'topologyfile' and 'coordinatefile' should be specified as same for extracting contactd from a PDB file.

Example:  trajcontacts -p 3sn6.pdb -f 3sn6.pdb -n 10


How to cite:

Madhu, M. K., et al. "Delineating the Biased Signaling Mechanism in Mutated Variants of β2-Adrenergic Receptor Using Molecular Dynamics Simulations"


Copyright: Computational Biophysics and Soft Matter Group, IISER Bhopal (https://home.iiserb.ac.in/~rkm/)
