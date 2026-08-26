# Cell 30 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df["Name"].to_string())
