# Cell 76 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df["Legendary"] = df["Legendary"].astype(bool)

print(df.to_string())
