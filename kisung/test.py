import json

# Dictionary with atomic numbers as keys
elements = {
    1: [1],    # H
    2: [2],    # He
    3: [3],    # Li
    4: [4],    # Be
    5: [5],    # B
    6: [6],    # C
    7: [7],    # N
    8: [8],    # O
    9: [9],    # F
    10: [10],  # Ne
    11: [11],  # Na
    12: [12],  # Mg
    13: [13],  # Al
    14: [14],  # Si
    15: [15],  # P
    16: [16],  # S
    17: [17],  # Cl
    18: [18],  # Ar
    19: [19],  # K
    20: [20],  # Ca
    25: [25],  # Mn
    28: [28],  # Ni
    51: [51],  # Sb
    73: [73],  # Ta
}

# Path for atom_init.json
atom_init_file = 'structures_cif/atom_init.json'  

# Write to JSON file with atomic numbers as keys
with open(atom_init_file, 'w') as f:
    json.dump(elements, f)

print(f"atom_init.json created at {atom_init_file} with atomic numbers as keys.")

