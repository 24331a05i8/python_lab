import pandas as pd

df = pd.read_csv("data.csv")

print(df[:3])
print(df["Marks"])

sorted_df = df.sort_values(by="Marks")
print(sorted_df)
