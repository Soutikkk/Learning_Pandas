# Cell 77 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df = df.drop_duplicates()

print(df.to_string())
