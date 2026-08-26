# Cell 15 | Section: Series

calories = {"Day 1" : 1750 , "Day 2" : 1800 , "Day 3" : 2000}

series = pd.Series(calories)

series.loc ["Day 1"] = 2000

print(series.loc["Day 1"])
