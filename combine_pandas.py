import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([5,np.nan,6,np.nan], index=['A','B','C','D'])
print (s1)

s2 = Series(np.arange(4),dtype=np.float64,index=s1.index)
print (s2)
#to replace the nan values in Series 1 with the corresponding values in Series 2, you can use the (np.where)function
s3 = Series(np.where(pd.isnull(s1),s2,s1),index=s1.index)
print (s3)
#or you can use the (combine_first) function which is shorter and faster
s4 = s1.combine_first(s2)
print (s4)

#combine function on dataframes
df_5m = DataFrame({'col1':[5,np.nan,15],'col2':[20,25,np.nan],'col3':[np.nan,np.nan,35]})
df_10m = DataFrame({'col1':[0,10,20],'col2':[10,20,30]})
print (df_5m)
print (df_10m)
print (df_5m.combine_first(df_10m))



