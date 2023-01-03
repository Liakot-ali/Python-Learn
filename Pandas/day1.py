import pandas as pd
import numpy as np

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