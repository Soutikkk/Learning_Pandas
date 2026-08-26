# Cell 73 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df["Name"] = df["Name"].str.upper()

print(df.to_string())
