'''
Alcohol Consumption vs Family Relationship

Uses pandas to sort the data and matplotlib to visualize
'''

import random
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('student-mat.csv')    
data2 = pd.read_csv('student-por.csv')
datatotal = pd.concat([data1, data2], ignore_index=True)

#Weekly Alcohol Consumption List
dataRelvlw = []  
dataRellw = []
dataRelmw = []
dataRelhw = []
dataRelvhw = []

#Daily Alcohol Consumption List
dataRelvld = []
dataRelld = []
dataRelmd = []
dataRelhd = []
dataRelvhd = []

#sort the data
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
datat = [dataRelvhw,dataRelhw,dataRelmw,dataRellw,dataRelvlw]

p = plt.boxplot(datat,patch_artist=True)
#Visualization tweaks
p['boxes'][0].set(facecolor='green')
p['boxes'][1].set(facecolor='lightgreen')
p['boxes'][2].set(facecolor='orange')
p['boxes'][3].set(facecolor='orangered')
p['boxes'][4].set(facecolor='red')
for line in p['medians']:
    line.set(color='blue')
plt.xticks([1,2,3,4,5],['Very Good', 'Good', "Ok", "Bad", "Very Bad"])
plt.xlabel('Family Relationship')
plt.ylabel('Alcohol (weekend)')
plt.show()


'''
#information displayed isnt as good
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