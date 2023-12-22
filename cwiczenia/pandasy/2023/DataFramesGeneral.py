import pandas as pd

dataFrame = pd.DataFrame([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
dataFrame2 = pd.DataFrame([[1, 2, 3], [4, 5], [6, 7, 8, 9]], index=['row1', 'row2', 'row3'], columns=['jedziemy1', 'jedziemy2', 'jedziemy3', 'jedziemy4'])
print(dataFrame)
print(dataFrame2)
print("----------------")
#columns
first_column = dataFrame2['jedziemy2']
second_column = dataFrame2.jedziemy2
third_column = dataFrame2.get('jedziemy3')
print(first_column)
print(second_column)
print(third_column)

#rows
print("rows------------------")
row1 = dataFrame.iloc[1]
print(row1)

#single elements
singleEl = dataFrame2['jedziemy3'].loc['row3']
print(singleEl)
singleUnknownRow = dataFrame2['jedziemy3'].iloc[2]
singleUnknownRowLoc = dataFrame2.loc['row3', 'jedziemy3']
singleUnknownRowiLoc = dataFrame2.iloc[2,2]
print(singleUnknownRow)
print(singleUnknownRowLoc)
print(singleUnknownRowiLoc)

#multiple rows/ columns
multipleUnknownRowiLoc = dataFrame2.iloc[[2,2]]
print(multipleUnknownRowiLoc)

#slicing
print("slicing---------------")
slicing = dataFrame2.iloc[:, :2]
print(slicing)

#booleans
bools = dataFrame2[dataFrame2['jedziemy3'] >= 5]
print(bools)

#parameters
print('===============')
count = dataFrame2.count(axis=1) #pion lub poziom
print(count)

desc = dataFrame2.describe()
print(desc)

n_largest = dataFrame2.nlargest(2, 'jedziemy1')
print(n_largest)
