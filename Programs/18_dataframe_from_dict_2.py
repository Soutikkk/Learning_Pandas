# Cell 19 | Section: Dataframes

import pandas as pd

data = {
    "Name": ["SpongeBob", "Patrick", "Sandy", "Squidward", "Mr. Krabs"],
    "Age": [20, 21, 19, 30, 45],
    "Occupation": ["Fry Cook", "Unemployed", "Scientist", "Cashier", "Business Owner"]
}

dataframe = pd.DataFrame(data,index=["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5"])

print(dataframe)
