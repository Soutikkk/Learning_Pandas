# Cell 44 | Section: Now will Learn About Filtering

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

lagendary_pokemon = df[df["Legendary"] == True]

print(lagendary_pokemon)
