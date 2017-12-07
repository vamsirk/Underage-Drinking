'''
WEEKEND VS DAILY ALCOHOL CONSUMPTION
                &
Number of students who drink in each category
'''
import random
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('student-mat.csv')    
data2 = pd.read_csv('student-por.csv')
datatotal = pd.concat([data1,data2], ignore_index=True)

#Weekend vs Daily Alcohol Consumption
#sorting the data into lists
dataWalcM = []
dataWalcF = []
dataDalcM = []
dataDalcF = []
for i,v in datatotal['sex'].iteritems():
    #uses random.uniform so points dont overlap as much
    if v == 'M':
        dataWalcM.append(random.uniform((datatotal['Walc'][i]-0.4),(datatotal['Walc'][i]+0.4)))
        dataDalcM.append(random.uniform((datatotal['Dalc'][i]-0.4),(datatotal['Dalc'][i]+0.4)))
    else:
        dataWalcF.append(random.uniform((datatotal['Walc'][i]-0.4),(datatotal['Walc'][i]+0.4)))
        dataDalcF.append(random.uniform((datatotal['Dalc'][i]-0.4),(datatotal['Dalc'][i]+0.4)))

plt.scatter(dataWalcM,dataDalcM,s=5,alpha=0.25)
plt.scatter(dataWalcF,dataDalcF,c='red',s=5,alpha=0.25)
plt.xlabel('Degree of Alcohol Consumption (Weekdend)')
plt.ylabel('Degree of Alcohol Consumption (Weekdays)')
blue_patch = mpatches.Patch(color='blue', label='Male')
red_patch = mpatches.Patch(color='red', label='Female')
plt.legend(handles=[red_patch,blue_patch])

plt.show()

#Number of students
studentsw = [0,0,0,0,0]
studentsd = [0,0,0,0,0]
for i,v in datatotal['Walc'].iteritems():
    studentsw[v-1] = studentsw[v-1]+1
for i,v in datatotal['Dalc'].iteritems():
    studentsd[v-1] = studentsd[v-1]+1

plt.subplot(1,2,1)
barlist = plt.bar([1,2,3,4,5], studentsw)
#Visualization tweaks
plt.xticks([1,2,3,4,5],['V Low','Low','Med', 'High', 'V High'])
plt.xlabel('Degree of Alcohol Consumption (Weekdend)')
plt.ylabel('Number of Students')
barlist[0].set_color('green')
barlist[1].set_color('lightgreen')
barlist[2].set_color('orange')
barlist[3].set_color('orangered')
barlist[4].set_color('r')

plt.subplot(1,2,2)
barlist = plt.bar([1,2,3,4,5], studentsd)
#Visualization tweaks
plt.xticks([1,2,3,4,5],['V Low','Low','Med', 'High', 'V High'])
plt.xlabel('Degree of Alcohol Consumption (Weekdays)')
plt.ylabel('Number of Students')
plt.tight_layout()
barlist[0].set_color('green')
barlist[1].set_color('lightgreen')
barlist[2].set_color('orange')
barlist[3].set_color('orangered')
barlist[4].set_color('r')
plt.show()