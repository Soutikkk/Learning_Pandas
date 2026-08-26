# Cell 70 | Section: Data Cleaning

import pandas as pd

df = pd.read_csv("Pokemon.csv")

df = df.fillna({"Type2" : "None"})

print(df.to_string())
