# Cell 43 | Section: Now will Learn About Filtering

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

tall_pokemon = df[df["Weight"] > 100]

print(tall_pokemon)
