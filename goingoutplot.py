import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data1 = pd.read_csv('student-mat.csv')    
data2 = pd.read_csv('student-por.csv')
datatotal = pd.concat([data1, data2], ignore_index=True)

#DAILY ALCOHOL
datavl = []
datal= []
datam = []
datah = []
datavh = []

dataDalc = pd.concat([data1['Dalc'],data2['Dalc']], ignore_index=True)
dataGOOUT = pd.concat([data1['goout'],data2['goout']], ignore_index=True)
for i,v in dataDalc.iteritems():
    if(v == 1):
        datavl.append(dataGOOUT[i])
    elif(v ==2):
        datal.append(dataGOOUT[i])
    elif(v ==3):
        datam.append(dataGOOUT[i])
    elif(v == 4):
        datah.append(dataGOOUT[i])
    elif(v == 5):
        datavh.append(dataGOOUT[i])
        
datat = [datavl,datal,datam,datah,datavh]     
p = plt.boxplot(datat)
plt.xlabel('Degree of Alcohol Consumption (Weekday)')
plt.ylabel('Degree of going out')
plt.show()

#WEEKEND ALCOHOL (Good)
dataGvl = []
dataGl= []
dataGm = []
dataGh = []
dataGvh = []

dataGvld = []
dataGld= []
dataGmd = []
dataGhd = []
dataGvhd = []

dataWalc = pd.concat([data1['Walc'],data2['Walc']], ignore_index=True)
dataDalc = pd.concat([data1['Dalc'],data2['Dalc']],ignore_index=True)
dataGOOUT = pd.concat([data1['goout'],data2['goout']], ignore_index=True)
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
p = plt.boxplot(datat)
plt.ylabel('Degree of Alcohol Consumption (Weekdend)')
plt.xlabel('Degree of going out')
plt.show()