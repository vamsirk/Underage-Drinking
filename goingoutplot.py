'''
Alcohol Consumption vs Going Out
'''

import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('student-mat.csv')    
data2 = pd.read_csv('student-por.csv')

#Weekly Alcohol Lists
dataGvl = []
dataGl= []
dataGm = []
dataGh = []
dataGvh = []

#Daily Alcohol Lists
dataGvld = []
dataGld= []
dataGmd = []
dataGhd = []
dataGvhd = []

#extract the data
dataWalc = pd.concat([data1['Walc'],data2['Walc']], ignore_index=True)
dataDalc = pd.concat([data1['Dalc'],data2['Dalc']],ignore_index=True)
dataGOOUT = pd.concat([data1['goout'],data2['goout']], ignore_index=True)
#sort the data
for i,v in dataGOOUT.iteritems():
    if(v == 1):
        dataGvl.append(dataWalc[i])
        dataGvld.append(dataDalc[i])
    elif(v ==2):
        dataGl.append(dataWalc[i])
        dataGld.append(dataDalc[i])
    elif(v ==3):
        dataGm.append(dataWalc[i])
        dataGmd.append(dataDalc[i])
    elif(v == 4):
        dataGh.append(dataWalc[i])
        dataGhd.append(dataDalc[i])
    elif(v == 5):
        dataGvh.append(dataWalc[i])
        dataGvhd.append(dataDalc[i])
        
datat = [dataGvl,dataGl,dataGm,dataGh,dataGvh]     
p = plt.boxplot(datat,patch_artist=True)

#Visualization tweaks
p['boxes'][0].set(facecolor='green')
p['boxes'][1].set(facecolor='lightgreen')
p['boxes'][2].set(facecolor='orange')
p['boxes'][3].set(facecolor='orangered')
p['boxes'][4].set(facecolor='red')
for line in p['medians']:
    line.set(color='blue')
plt.ylabel('Degree of Alcohol Consumption (Weekdend)')
plt.xlabel('Degree of going out')

plt.show()