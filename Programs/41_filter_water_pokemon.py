# Cell 45 | Section: Now will Learn About Filtering

import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

water_pokemon = df[df["Type1"] == "Water"]

print(water_pokemon)
