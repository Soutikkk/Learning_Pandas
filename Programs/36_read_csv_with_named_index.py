# Cell 39 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

print(df.iloc[0:11:2])
