import pandas as pd
import numpy as np
# Convert Series of lists to one Series
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)

#  Write a Pandas program to sort a given Series.
sort = pd.Series(['100', '200', 'python', '300.12', '400'])
sort = sort.sort_values()
print(sort)

#  Calculate the frequency counts of each unique value of a given series
# ser = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
ser = pd.Series(np.random.randint(0, 10, 40))
count = ser.value_counts().sort_values()
print(count)

# Find the index of the first occurrence of the smallest and largest value of a given series
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print(nums.idxmax())
print(nums.idxmin())


# Join two dataframes along columns
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
        'marks': [201, 200, 198, 219, 201]})

all_student = pd.concat([student_data1, student_data2], axis=0)
all_student_new_index = pd.concat([student_data1, student_data2], axis=0).reset_index(drop=True)
print(all_student)
print(all_student_new_index)

# Write a Pandas program to join (left join) the two dataframes using keys from left dataframe only
merged_data = pd.merge(student_data1, student_data2, how="left", on=["student_id"])
print(merged_data)
