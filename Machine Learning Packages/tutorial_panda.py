# %% Pandas

''' Pandas is a popular Python library for data analysis. It is not directly related to Machine Learning.
As we know that the dataset must be prepared before training. In this case, Pandas comes handy as it was developed specifically
for data extraction and preparation. It provides high-level data structures and wide variety tools for data analysis.
It provides many inbuilt methods for groping, combining and filtering data.
'''

# importing pandas as pd
import pandas as pd
import numpy as np


def exSeries():
        s1 = pd.Series([12, -4, 7, 9])
        print(s1) # indices are in sequential order starting from 0

        s2 = pd.Series([12, -4, 7, 9], index = ['a', 'b', 'c', 'd']) #  optional indices
        print(s2)

        print(s1.values)
        print(s1.index)
        print(s1[2])
        print(s2['b'])
        print(s1[0:2])
        print(s2[['b','c']])

        s1[1] = 0
        print(s1)
        s2['b'] = 1
        print(s2)

        arr = np.array([1, 2, 3, 4])
        s3 = pd.Series(arr)
        print(s3)

        print(s1[s1 > 8]) # filtering
        print(s1 /2) # math

        serd = pd.Series([1, 0, 2, 1, 2, 3], index = ['white', 'white', 'blue', 'green', 'green', 'yellow'])
        print(serd.unique()) # unique
        print(serd.value_counts()) # counts how many
        print(serd.isin([0, 3]))  # is in there
        print(serd[serd.isin([0, 3])])

        s3 = pd.Series([5, -3, np.NaN, 14])
        print(s3)
        print(s3.isnull())
        print(s3.notnull())
        print(s3[s3.notnull()])

        # series can be think of a dictionary
        mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
        myseries = pd.Series(mydict)
        print(myseries)

        # If there is a mismatch create NaN
        colors = ['red', 'yellow', 'orange', 'blue', 'green']
        myseries = pd.Series(mydict, index=colors)

# Python program using Pandas for arranging a given set of data into a  table
def exDataFrame():
        data = {"color": ["blue", "green", "yellow", "red", "white"],
                "object": ["ball", "pen", "pencil", "paper", "mug"],
                "price": [1.2, 1.0, 0.6,0.9, 1.7]}

        frame = pd.DataFrame(data)
        print(frame)
        print(frame['price']) # als0 frame.price
        print(frame.loc[2])
        print(frame.loc[[2,4]])

        print(frame[0:1])
        print(frame['object'][3])
        print(frame.isin([1.0,'pen']))
        print(frame[frame.isin([1.0,'pen'])])

        print(frame[frame < 1.2])

def exMath():
        frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                             index = ['red', 'blue', 'yellow', 'white'],
                             columns = ['ball', 'pen', 'pencil', 'paper'])
        print(frame)
        print(np.sqrt(frame))
        f = lambda x: x.max() - x.min()
        print(frame.apply(f)) # apply column-wise
        print(frame.apply(f, axis = 1)) # apply row-wise
        print(frame.sum())
        print(frame.mean())
        print(frame.describe())
        print(frame.sort_index())
        print(frame.sort_index(axis=1))

def readCSV():
        csvframe = pd.read_csv('readCSV.csv')
        print(csvframe)

if __name__ == '__main__':
        # exSeries()
        # exDataFrame()
        # exMath()
        readCSV()