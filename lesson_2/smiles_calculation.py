from rdkit.Chem import MolFromSmiles, Descriptors

all_smiles = [
    'CC(CCC(=O)N)CN',
    'C#C',
    'CC1=CC(NC(=O)NC2=CC=C(C=C2)C2=C3C(N)=NNC3=CC=C2)=C(F)C=C1',
    'CNC(=O)C1=CC=CC=C1SC1=CC2=C(C=C1)C(\C=C\C1=CC=CC=N1)=NN2',
    'CN1C=NC2=C(F)C(NC3=CC=C(Br)C=C3Cl)=C(C=C12)C(=O)NOCCO',
    'CN(C)C1CCN(CC2=CC=C(C=C2C(F)(F)F)C(=O)NC2=CC=C(C)C(NC3=NC=CC(=N3)C3=CN=CN=C3)=C2)C1',
]

smiles = all_smiles[0]
mol = MolFromSmiles(smiles)
mol_properties = {
    'smiles': smiles,
    'Molecular weight': Descriptors.MolWt(mol),
    'logP': Descriptors.MolLogP(mol),
    'H Acceptors': Descriptors.NumHAcceptors(mol),
    'H Donors': Descriptors.NumHDonors(mol),
}
print(mol_properties)
# TODO Добавить в словарь свойство lipinski pass, которое равно True, если:
# - Молекулярный вес меньше 500
# - logP меньше 5
# - H Donors меньше 5
# - H Acceptors меньше 10

# TODO рассчитать свойства для всех молекул, а не только для первой
#  и сохранить их в массив

# TODO отфильтровать те молекулы, у которых значение lipinsli pass - True.
#  Сохранить в отдельных массив

