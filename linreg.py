
# coding: utf-8

# In[16]:


import pandas as pd
from pandas import DataFrame as df
import numpy as np
data1 = pd.read_csv('student-mat.csv')
data2 = pd.read_csv('student-por.csv')
data = [data1,data2]
data1.describe()
data1.head()
list(data1.columns)
#check if need filling data
data1.isnull()
mod_data1 = data1
binaryYesNo = {'yes': 1, 'no': 0}
school_map  = {'MS': 1, 'GP': 2}
sex_map     = {'M': 1, 'F': 2}
address_map = {'R':1, 'U':2}
famsize_map = {'LE3':1, 'GT3':2}
pstatus_map = {'A':1, 'T':2}
mjob_map    = {'services' : 1, 'health' : 2, 'other' : 3, 'at_home' : 4, 'teacher' : 5}
fjob_map    = {'services' : 1, 'health' : 2,  'other' : 3,  'at_home' : 4, 'teacher' : 5}
reason_map   = {'course':1, 'other':2, 'reputation':3, 'home':4}
guardian_map = {'other':0, 'father':1, 'mother':1}
mod_data1.schoolsup  = mod_data1.schoolsup.map(binaryYesNo)
mod_data1.famsup     = mod_data1.famsup.map(binaryYesNo)
mod_data1.paid       = mod_data1.paid.map(binaryYesNo)
mod_data1.activities = mod_data1.activities.map(binaryYesNo)
mod_data1.nursery    = mod_data1.nursery.map(binaryYesNo)
mod_data1.higher     = mod_data1.higher.map(binaryYesNo)
mod_data1.internet   = mod_data1.internet.map(binaryYesNo)
mod_data1.romantic   = mod_data1.romantic.map(binaryYesNo)
mod_data1.school   = mod_data1.school.map(school_map)
mod_data1.sex      = mod_data1.sex.map(sex_map)
mod_data1.address  = mod_data1.address.map(address_map)
mod_data1.famsize  = mod_data1.famsize.map(famsize_map)
mod_data1.Pstatus  = mod_data1.Pstatus.map(pstatus_map)
mod_data1.Mjob     = mod_data1.Mjob.map(mjob_map)
mod_data1.Fjob     = mod_data1.Fjob.map(fjob_map)
mod_data1.reason   = mod_data1.reason.map(reason_map)
mod_data1.guardian = mod_data1.guardian.map(guardian_map)
mod_data1.head()
from sklearn.linear_model import LinearRegression
lm1 = LinearRegression()
#drop the consumption columns
X1 = mod_data1.drop('Dalc',axis =1)
X = X1.drop('Walc',axis =1)
#create new columns for total consumption 'Talc'
mod_data1['Talc'] = mod_data1['Dalc']+mod_data1['Walc']
#fit a linear regression model for consumption
lm1.fit(X,mod_data1.Walc)
#print the coefficient
variables = pd.DataFrame(zip(X.columns, lm1.coef_),columns = ['variables', 'estimated_Coefficients'])
variables['absolutevalues'] = abs(variables['estimated_Coefficients'])
mod_var = variables.sort_values(by = ['absolutevalues'],ascending = False)
imp_var = mod_var.head(8)
#so the most 5 important variables for alcohal consumptionare listed below
'''
   variables  estimated_Coefficients  absolutevalues
1        sex               -0.527022        0.527022
25     goout                0.443077        0.443077
11  guardian                0.432784        0.432784
17      paid                0.370493        0.370493
19   nursery               -0.317861        0.317861
3    address               -0.296834        0.296834
23    famrel               -0.227899        0.227899
0     school                0.216776        0.216776
'''


# In[17]:


with open('./output.txt', 'w') as f:
    f.write(_)
#fit a linear regression model for Final grade
lm2 = LinearRegression()
X1 = mod_data1.drop('G1',axis =1)
X2 = X1.drop('G2',axis =1)
X = X2.drop('G3',axis =1)
lm2.fit(X,mod_data1.G3)
variables2 = pd.DataFrame(zip(X.columns, lm2.coef_),columns = ['variables', 'estimated_Coefficients'])
variables2['absolutevalues'] = abs(variables2['estimated_Coefficients'])
mod_var2 = variables2.sort_values(by = ['absolutevalues'],ascending = False)
imp_var2 = mod_var2.head(8)
#so the most 5 important variables for final grade are listed below
'''
    variables  estimated_Coefficients  absolutevalues
14   failures               -1.700897        1.700897
15  schoolsup               -1.311088        1.311088
1         sex               -1.115701        1.115701
22   romantic               -1.020906        1.020906
20     higher                1.013433        1.013433
16     famsup               -0.816223        0.816223
0      school               -0.740585        0.740585
4     famsize               -0.678850        0.678850
'''


# In[18]:


with open('./output2.txt', 'w') as f:
    f.write(_)


# In[ ]:




