# Cell 37 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

print(df.loc["Charizard", ["Height", "Weight"]])
