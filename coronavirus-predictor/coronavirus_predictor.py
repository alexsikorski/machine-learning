import pandas as pd

fields = ['World']  # only obtaining world column
df = pd.read_csv('total_cases.csv', skipinitialspace=True, usecols=fields)
print(df.head())

