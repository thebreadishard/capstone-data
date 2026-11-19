"""Are the five fluoranthene-containing molecules v1.4's measurement networks trained on all benzo[k]fluoranthene derivatives?"""
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold

BKF = Chem.CanonSmiles("c1ccc2cc3c(cc2c1)-c1cccc2cccc-3c12")
FIVE = ["COc1ccc2cc3c(cc2c1)-c1cccc2cccc-3c12", "FC(F)(F)c1ccc2cc3c(cc2c1)-c1cccc2cccc-3c12",
        "O=Cc1ccc2cc3c(cc2c1)-c1cccc2cccc-3c12", "Sc1ccc2cccc3c2c1-c1cc2ccccc2cc1-3", "c1ccc2cc3c(cc2c1)-c1cccc2cccc-3c12"]
for s in FIVE:
    scaffold = Chem.CanonSmiles(MurckoScaffold.MurckoScaffoldSmiles(s))
    print(s, scaffold == BKF)
