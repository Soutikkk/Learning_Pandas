# Cell 9 | Section: Series

data = [100 , 102 , 104]
series = pd.Series(data, index= ["a" , "b" , "c"])
series.loc["a"] = 200
print(series.loc["a"])
