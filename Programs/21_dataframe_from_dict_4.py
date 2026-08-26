# Cell 22 | Section: Dataframes

import pandas as pd

data = {
    "Name": ["SpongeBob", "Patrick", "Sandy", "Squidward", "Mr. Krabs"],
    "Age": [20, 21, 19, 30, 45],
    "Occupation": ["Fry Cook", "Unemployed", "Scientist", "Cashier", "Business Owner"]
}

dataframe = pd.DataFrame(
    data,
    index=["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5"]
)

# Add a new column
dataframe["Salary"] = [30000, 25000, 40000, 35000, 50000]

# Add a new row
new_employee = pd.DataFrame(
    {
        "Name": ["Plankton"],
        "Age": [35],
        "Occupation": ["Restaurant Owner"],
        "Salary": [60000]
    },
    index=["Employee 6"]
)

dataframe = pd.concat([dataframe, new_employee])

print(dataframe)
