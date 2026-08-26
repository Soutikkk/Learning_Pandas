# Cell 71 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df["Type2"] = df["Type2"].replace({"Grass": "GRASS"})

print(df.to_string())
