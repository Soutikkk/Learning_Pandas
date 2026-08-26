# Cell 32 | Section: Now we will learn about Selection Techniques

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df["Weight"].to_string())
