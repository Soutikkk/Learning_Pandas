# Cell 16 | Section: Series

calories = {"Day 1" : 1750 , "Day 2" : 1800 , "Day 3" : 2000}

series = pd.Series(calories)

print(series[series > 1800])
