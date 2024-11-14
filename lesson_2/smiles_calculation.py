import csv

from rdkit.Chem import MolFromSmiles, Descriptors


def save_molecules(output_filename, records):
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in records:
            writer.writerow(row)


all_smiles = [
    'CC(CCC(=O)N)CN',
    'C#C',
    'CC1=CC(NC(=O)NC2=CC=C(C=C2)C2=C3C(N)=NNC3=CC=C2)=C(F)C=C1',
    'CNC(=O)C1=CC=CC=C1SC1=CC2=C(C=C1)C(\C=C\C1=CC=CC=N1)=NN2',
    'CN1C=NC2=C(F)C(NC3=CC=C(Br)C=C3Cl)=C(C=C12)C(=O)NOCCO',
    'CN(C)C1CCN(CC2=CC=C(C=C2C(F)(F)F)C(=O)NC2=CC=C(C)C(NC3=NC=CC(=N3)C3=CN=CN=C3)=C2)C1',
]


all_mol_properties = []
for smiles in all_smiles:
    mol = MolFromSmiles(smiles)
    mol_properties = {
        'smiles': smiles,
        'Molecular weight': Descriptors.MolWt(mol),
        'logP': Descriptors.MolLogP(mol),
        'H Acceptors': Descriptors.NumHAcceptors(mol),
        'H Donors': Descriptors.NumHDonors(mol),
    }

    mol_properties['Lipinski'] = (
        mol_properties['Molecular weight'] <= 500
        and mol_properties['logP'] < 5
        and mol_properties['H Acceptors'] < 10
        and mol_properties['H Donors'] < 5
    )

    all_mol_properties.append(mol_properties)

filtered_records = []
for record in all_mol_properties:
    if record['Lipinski']:
        filtered_records.append(record)

filtered_records = [
    record for record in all_mol_properties
    if record['Lipinski']
]

save_molecules('filtered_records.csv', filtered_records)
