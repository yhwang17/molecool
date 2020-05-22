import os
import numpy as np
import matplotlib.pyplot as plt
from .measure import calculate_distance

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """
    Calculate the bonds in a moleculae based on a distance critera

    Parameters
    ----------
    coorindates : np.ndarray
        The coordinates of the atoms
    max_bound : float (optional)
        The maximum distance for two atome to be considered bonded.

    Returns
    -------
    bonds : dict
        A dictionary where the keys are tuples of the bonded atom indices, and the associated
        values are the bound lengths.

    
    """

    if min_bond < 0:
        raise ValueError("Minimum bound length can not be less than zero!")
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
