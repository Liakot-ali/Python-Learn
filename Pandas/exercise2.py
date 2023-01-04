import pandas as pd
diamonds = pd.read_csv('diamonds.csv')
print(diamonds.head())

# Write a Pandas program to read a dataset from diamonds DataFrame and modify the default columns values and print the first 6 rows.
# print("\n\nAfter changing column name")
# diamonds.columns = list('ABCDEFGHIJ')
# print(diamonds.head(6))

# Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series
print(diamonds['depth'])
print(diamonds.dtypes)

# Write a Pandas program to create a new 'Quality -color' Series (use bracket notation to define the Series name) of the diamonds DataFrame
diamonds["Quality-color"] = diamonds['cut'] + ',' + diamonds['color']
# diamonds["Quality-color"] = diamonds.cut + ',' + diamonds.color
print(diamonds.head())

# Write a Pandas program to remove multiple columns at once of the diamonds Dataframe
diamonds_rmv_column = diamonds.drop(['cut', 'color'], axis=1)
print(diamonds_rmv_column)

# Write a Pandas program to sort the entire diamonds DataFrame by the 'carat' Series in ascending and descending order.
diamonds_sort = diamonds.sort_values('carat')
print(diamonds_sort)

# Write a Pandas program to filter the DataFrame rows to only show carat weight at least 1.0
diamonds_carat_0_3 = diamonds.loc[diamonds['carat'] >= 1.0]
print(diamonds_carat_0_3)
