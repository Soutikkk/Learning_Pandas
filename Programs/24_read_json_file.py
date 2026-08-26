# Cell 26 | Section: Now we will learn about importing CSV and JSON file in Pandas

import pandas as pd

df = pd.read_json("Pokemon2.json")

print(df.to_string())
