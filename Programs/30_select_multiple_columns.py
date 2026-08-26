# Cell 33 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df[["Name", "Height", "Weight"]].to_string())
