#family relationships
import random
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data1 = pd.read_csv('student-mat.csv')    
data2 = pd.read_csv('student-por.csv')
datatotal = pd.concat([data1, data2], ignore_index=True)

dataRelvlw = []
dataRellw = []
dataRelmw = []
dataRelhw = []
dataRelvhw = []

dataRelvld = []
dataRelld = []
dataRelmd = []
dataRelhd = []
dataRelvhd = []

for i,v in datatotal['famrel'].iteritems():
    if(v == 1):
        dataRelvlw.append(datatotal['Walc'][i])
        dataRelvld.append(datatotal['Dalc'][i])
    if(v == 2):
        dataRellw.append(datatotal['Walc'][i])
        dataRelld.append(datatotal['Dalc'][i])
    if(v == 3):
        dataRelmw.append(datatotal['Walc'][i])
        dataRelmd.append(datatotal['Dalc'][i])
    if(v == 4):
        dataRelhw.append(datatotal['Walc'][i])
        dataRelhd.append(datatotal['Dalc'][i])
    if(v == 5):
        dataRelvhw.append(datatotal['Walc'][i])
        dataRelvhd.append(datatotal['Dalc'][i])
datat = [dataRelvlw,dataRellw,dataRelmw,dataRelhw,dataRelvhw]
p = plt.boxplot(datat)
plt.xlabel('Family Relationship')
plt.ylabel('Alcohol (weekend)')
plt.show()
print [len(datatotal['famrel']),len(dataRelvlw), len(dataRellw), len(dataRelmw), len(dataRelhw), len(dataRelvhw)]
#this one is good because we can see that from 4 to 3 the median is the same but the median of the other quartile goes up a whole level. and then 3 to 2 the median goes up

'''
#not good
datat = [dataRelvld,dataRelld,dataRelmd,dataRelhd,dataRelvhd]
p = plt.boxplot(datat)
plt.show()

#not that good either
#averaged out version of the combination of weekend and daily
from operator import add
from operator import div
p = plt.boxplot([[a/2 for a in map(add,dataRelvlw,dataRelvld)], [a/2 for a in map(add,dataRellw,dataRelld)],[a/2 for a in map(add,dataRelmw,dataRelmd)],[a/2 for a in map(add,dataRelhw,dataRelhd)],[a/2 for a in map(add,dataRelvhw,dataRelvhd)]])
plt.show()
'''