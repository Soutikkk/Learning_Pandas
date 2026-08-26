# Cell 65 | Section: Now we would Learn about Aggregation

import pandas as pd

df = pd.read_csv("Pokemon.csv")

group = df.groupby("Type1")["Height"].count()

print(group)
