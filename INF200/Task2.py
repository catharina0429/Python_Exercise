# Week 40 Assignment
"""Task 2—From records to dataframes"""

import pandas as pd

data = [{'name': 'Joe', 'age': 22, 'phone': '12345678'},
         {'name': 'Pia', 'age': 24, 'phone': '23456789'},
          {'name': 'Even', 'age': 21, 'phone': '34567890'},
           {'name': 'Abdul', 'age': 23, 'phone': '45678901'}]

print(type(data))
df = pd.DataFrame(data)
print(df)
print("The average age of the student is : ", df['age'].mean())
# print(df[0:1])