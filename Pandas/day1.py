import pandas as pd
import numpy as np
import openpyxl as xl

# Pandas series
ser = pd.Series(np.random.randint(1, 100, 50))
print(ser.head(10))
print(ser.describe())
print(ser.tail(11))
print(ser[45])

arr = ser.to_numpy()
print(arr)

# Pandas DataFrame

df = pd.DataFrame(np.random.randint(15, 20, (20, 5)))
df.columns = list('ABCDE')
print(df)
print(df.dtypes)
print(df.describe())
print(df.T)
dfUp = df.drop('B', axis=1)
print(df, dfUp)

print(df)
df.loc[0, 'B'] = 24
print(df)
# Print where Column A is only 15
print(df['A'] == 16)  # It returns true or false of the column A
print(df.loc[df['A'] == 15])

# Read CSV and XLSX

file1 = pd.read_csv("example.csv")
print(file1)

try:
    file2 = pd.read_excel("file1.xlsx")
    print(file2)
except ImportError as ie:
    print("Import error : ", ie)

df.to_csv("random.csv")
df.to_excel("rand.xlsx")