#GUARDIAN 2
import random
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data1 = pd.read_csv('student-mat.csv')    
data2 = pd.read_csv('student-por.csv')
datatotal = pd.concat([data1, data2], ignore_index=True)

dataGMw = []
dataGFw = []
dataGOw = []
dataGMd = []
dataGFd = []
dataGOd = []

for i,v in datatotal['guardian'].iteritems():
    if(v == 'mother'):
        dataGMw.append(random.uniform(datatotal['Walc'][i]-0.4,datatotal['Walc'][i]+0.4))
        dataGMd.append(random.uniform(datatotal['Dalc'][i]-0.4,datatotal['Dalc'][i]+0.4))
    if(v == 'father'):
        dataGFw.append(random.uniform(datatotal['Walc'][i]-0.4,datatotal['Walc'][i]+0.4))
        dataGFd.append(random.uniform(datatotal['Dalc'][i]-0.4,datatotal['Dalc'][i]+0.4))
    if(v == 'other'):
        dataGOw.append(random.uniform(datatotal['Walc'][i]-0.4,datatotal['Walc'][i]+0.4))
        dataGOd.append(random.uniform(datatotal['Dalc'][i]-0.4,datatotal['Dalc'][i]+0.4))

x = [random.uniform(0.6,1.4) for val in range(len(dataGMw))]
x1 = [random.uniform(1.6,2.4) for val in range(len(dataGFw))]
x2 = [random.uniform(2.6,3.4) for val in range(len(dataGOw))]

#Guardian vs Alcohol Consumption (weekdays)
plt.subplot(1, 2, 1)
p = plt.scatter(x, dataGMw, c='blue', s=5)
p2 = plt.scatter(x1, dataGFw, c='red', s=5)
p3 = plt.scatter(x2, dataGOw, c='green', s=5)
plt.xlabel('Guardian')
plt.ylabel('Degree of Alcohol Consumption (Weekdays)')
blue_patch = mpatches.Patch(color='blue', label='Mother')
red_patch = mpatches.Patch(color='red', label='Father')
green_patch = mpatches.Patch(color='green', label='Other')
plt.legend(handles=[red_patch,blue_patch, green_patch])

#Guardian vs Alcohol Consumption (Weekends)
plt.subplot(1, 2, 2)
pd = plt.scatter(x, dataGMd, c='blue', s=5)
pd2 = plt.scatter(x1, dataGFd, c='red', s=5)
pd3 = plt.scatter(x2, dataGOd, c='green', s=5)
plt.xlabel('Guardian')
plt.ylabel('Degree of Alcohol Consumption (Weekdend)')
blue_patch = mpatches.Patch(color='blue', label='Mother')
red_patch = mpatches.Patch(color='red', label='Father')
green_patch = mpatches.Patch(color='green', label='Other')
plt.legend(handles=[red_patch,blue_patch, green_patch])
plt.tight_layout()
plt.show()

'''
#Notes. Percents of how many people lie in each category
from collections import Counter
print Counter(map(round,dataGMd))
#38%  23% 18% 13% 7% total: 455q
# 72 17 6 2 3d
print Counter(map(round,dataGFd))
#37% 24% 18%  13% 8% total 153q
#64 23 8 3 2d
print Counter(map(round,dataGOd))
#39% 17% 24%  17% 2% total:41q
#53 23 10 10 5d
'''