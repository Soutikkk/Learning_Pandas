# Cell 68 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df = df.drop(columns=["Legendary", "No"], errors="ignore")

print(df)
