# Cell 67 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df = df.drop(columns=["Legendary"])

print(df)
