# Cell 42 | Section: Now will Learn About Filtering

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

tall_pokemon = df[df["Height"] >= 2.0]

print(tall_pokemon)
