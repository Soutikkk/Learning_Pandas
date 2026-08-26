# Cell 52 | Section: Now we would Learn about Aggregation

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df.min(numeric_only=True))
