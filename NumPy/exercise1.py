import numpy as np
# Write a NumPy program to display all the dates for the month of January, 2023
dates = np.arange('2023-01', '2024-01', dtype="datetime64[D]")
print(dates)

# Write a NumPy program to get the dates of yesterday, today and tomorrow.
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("today: ", today)
print("Yesterday: ", yesterday)
print("Tomorrow: ", tomorrow)

# Write a NumPy program to find the first Monday in January 2023.
date = np.busday_offset('2023-01', 0, roll='forward', weekmask='Mon')
print(date)

# Write a NumPy program to find the number of weekdays in March 2017.
weekday = np.busday_count('2023-01', '2023-02', weekmask='Sun')
print(weekday)