import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import random

B1 = np.arange(25).reshape(5,5)
A1 = random.randn(25).reshape(5,5)
print (B1)
print (A1)
print ("output for axis 1")
print (np.concatenate([A1,B1],axis=1))
print ("output for axis 0")
print (np.concatenate([A1,B1],axis=0))

#pandas dataframe - Series Concatenation
s1 = Series([100,200,300,400],index=['A','B','C','D'])
s2 =Series([100,200,300,400,500],index=['A','B','C','D','E'])
print (pd.concat([s1,s2]))
print ("axis 1 concatenation")
print (pd.concat([s1,s2],axis=1, ignore_index=True))

#pandas dataframe concatenation
df1 = DataFrame(random.rand(4,3),columns=['A','B','C'])
df2 = DataFrame(random.rand(3,3),columns=['D','E','F'])
print ("pd.concat dataframes")
print (pd.concat([df1,df2]))
#to have a continous index when you concatenate
print ("pd.concat dataframe  .  CONTINOUS INDEX")
print (pd.concat([df1,df2],ignore_index=True))

