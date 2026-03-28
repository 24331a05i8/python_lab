import pandas as pd

df = pd.read_csv("data.csv")

print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())

print("\nInformation:")
df.info()

print("\nStatistical Summary:\n", df.describe())