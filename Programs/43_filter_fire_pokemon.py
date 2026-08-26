# Cell 47 | Section: Now will Learn About Filtering

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

fire_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]

print(fire_pokemon)
