# Cell 69 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df = df.dropna(subset=["Type2"])

print(df.to_string())
