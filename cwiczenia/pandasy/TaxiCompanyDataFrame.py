import pandas as pd
dest = pd.read_csv("dest.csv")
dest.head
print(dest)

tips = pd.read_csv("tips.csv")
tips.head
print(tips)

prawdziwyDataFrame = pd.read_csv("WHO_first9cols.csv")


df_inner = pd.merge(dest, tips, on='EmpNr', how='inner')
print(df_inner)

df_outer = pd.merge(dest, tips, on='EmpNr', how='outer')
print(df_outer)

df_right = pd.merge(dest, tips, on='EmpNr', how='right')
print(df_right)

sumOfNulls = pd.isnull(prawdziwyDataFrame).sum()
print("Sum of nulls", sumOfNulls)