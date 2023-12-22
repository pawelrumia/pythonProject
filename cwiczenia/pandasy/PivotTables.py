import pandas as pd

purchase = pd.read_csv("purchase.csv")
print(purchase.head())

result = pd.pivot_table(purchase, values='Number', index=['Weather'], columns=['Food'])

print(result)
