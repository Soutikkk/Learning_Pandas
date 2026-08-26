# Cell 8 | Section: Series

data = [100 , 102 , 104]
series = pd.Series(data, index= ["a" , "b" , "c"])
print(series.loc["a"])
