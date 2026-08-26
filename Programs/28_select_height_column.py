# Cell 31 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df["Height"].to_string())
