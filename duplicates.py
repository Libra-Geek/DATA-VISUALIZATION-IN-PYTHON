import pandas as pd
from pandas import DataFrame

df = DataFrame({'col1':['Uber','Uber','Uber','Uber','Grab'], 'col2':[5,4,3,3,5]})
print (df)

#to find the duplicates in the dataframe
print(df.duplicated())

#how to drop the duplicates
print (df.drop_duplicates())

#where we want to eliminate duplicate values on a column
print (df.drop_duplicates(['col1']))

#where we want to eliminate the values before the last value in a dataframe
print (df.drop_duplicates(['col1'], keep='last'))
