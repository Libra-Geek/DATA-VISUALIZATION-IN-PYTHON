import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame

url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
df_list= pd.read_csv(url)
print (df_list)

excelfile = pd.ExcelFile('PIVOT DATA.xlsx')
dframe = excelfile.parse('Sheet1')
print ("PIVOT DATA RESULTS")
print (dframe)

table= pd.pivot_table(dframe,index=['year','continent','lifeExp'])
print ("PIVOT TABLE")
print (table)
print (table.plot(kind = 'bar'));

sns.heatmap(table).get_figure().savefig('heatmapassignment.png')