import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.tail())
df.info()
print(df.describe())

