# Cell 25 | Section: Now we will learn about importing CSV and JSON file in Pandas

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df.to_string())
