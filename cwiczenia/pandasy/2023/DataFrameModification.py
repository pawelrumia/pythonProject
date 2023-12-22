import pandas as pd
import numpy as np

dataFrame = pd.DataFrame([[1, 2, 3], [4, 5], [6, 7, 8, 9]], columns=['0', '1', '2', '3'])
dataFrame2 = pd.DataFrame([[1, 6, 4], [1, 8], [4, 2, 11, 18]], index=['row1', 'row2', 'row3'], columns=['jedziemy1', 'jedziemy2', 'jedziemy3', 'jedziemy4'])
dataFrame3 = pd.DataFrame([[3, 5, 9], [5, 11], [7, 1, 10, 7]], index=['row1', 'row2', 'row3'], columns=['jedziemy1', 'jedziemy2', 'jedziemy3', 'jedziemy4'])
dataFrame4 = pd.DataFrame([[1, 6, 4], [1, 8], [4, 2, 11, 18]], index=['row1', 'row2', 'row3'], columns=['jedziemy1', 'jedziemy2', 'jedziemy3', 'jedziemy4'])

print(dataFrame)
print(dataFrame2)

dataFrame2['kolumna4'] = [9,10, 11]
dataFrame2 = dataFrame2.append(pd.Series([15,16,17,18, 77],index=['jedziemy1', 'jedziemy2', 'jedziemy3', 'jedziemy4', 'kolumna4']), ignore_index=True)
print(dataFrame2)

# dropped = dataFrame2.dropna(axis=1)
# print(dropped)

dataFrame2['jedziemy3'] = [33, 34, 35, 36]
print(dataFrame2)

dataFrame2.loc['row1'] = [66,67,68,69,70]
print(dataFrame2)


print("operations")
def simpleFunction(x):
    return (3 * x) + 1.1

print("BEFORE")
print(dataFrame)
print("AFTER")
result = dataFrame.apply(simpleFunction)
print(result)
result = dataFrame.transform(lambda x: (3 * x) + 1.1)
print(result)
#róznica miedzy apply a transaform jest taka, ze transform przyjmuje kilka funkcji jednoczesnie
transformed = dataFrame.transform([np.log, np.square])
print(transformed)

transformedPartialy = dataFrame.transform({'0': np.log, '1': np.square})
print(transformedPartialy)

transposed = dataFrame2.transpose()
print(transposed)

print("SORTING")
sorted = dataFrame.sort_index(axis=1, ascending=True)
print(sorted)

sortedByValues = dataFrame2.sort_values('jedziemy3', axis=0, ascending=False)
print(sortedByValues)

print("POROWNANIE")
compared = dataFrame3.__gt__(dataFrame4)
print(compared)

print("Printing values")
for col_name, row_value in dataFrame2.items():
    print(col_name)
    print(row_value)

#to samo printuje tylko po rzedach:
for row_name, col_value in dataFrame2.iterrows():
    print(row_name)
    print(col_value)

print("Print standard data frame")
print(dataFrame2)