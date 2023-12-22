import pandas as pd

data_frame_generic = pd.DataFrame(84, index=['a', 'b', 'c'], columns=['col1', 'col2', 'col3', 'col4'])
data_frame = pd.DataFrame([[1, 2, 3],[4, 5],[7, 8, 9, 10,11]],  index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3', 'kolu4', 'kol5'])
print(data_frame)
print(data_frame_generic)
