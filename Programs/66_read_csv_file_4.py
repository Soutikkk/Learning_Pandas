# Cell 72 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})

print(df.to_string())
