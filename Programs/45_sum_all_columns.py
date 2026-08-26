# Cell 50 | Section: Now we would Learn about Aggregation

import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df.sum(numeric_only=True))
