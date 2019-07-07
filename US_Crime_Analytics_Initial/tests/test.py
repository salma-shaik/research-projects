import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), index=['Utah', 'Ohio','Texas', 'Oregon'])

series = frame.iloc[0]
# print(series.index)
print(frame)
print()
# series2 = pd.Series(range(3), index=['b','e','f'])
# print(series2)
# print()
# print(frame+series2)

series3 = frame['d']

# print(series3)

print(frame.sub(series3, axis='index'))