# Cell 40 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

pokemon = input("Enter the name of the Pokemon: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"Pokemon '{pokemon}' not found in the dataset.")
