import matplotlib.pyplot as plt
import csv
import numpy as np

'''
Index 0 One crop
Index 1 Multiple crops
Index 2 Fallow
Index 3 Pasture
Index 4 Home garden or irregular

First number is inside the field, second is total
'''
data = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

with open(survey_0.csv, mode = 'r')as csv_file
    csv_reader = csv.reader(csv_file, delimiter=',')
    rowiter=0
    for row in csv_reader
        if rowiter==0
            rowiter+=1
        else
            if (row[9]==One crop)
                if row[8]==Inside the field
                    data[0][0]+=1
                data[0][1]+=1
            elif row[9]==Multiple crops
                if row[8]==Inside the field
                    data[1][0]+=1
                data[1][1]+=1
            elif row[9]==Fallow
                if row[8]==Inside the field
                    data[2][0]+=1
                data[2][1]+=1
            elif row[9]==Pasture
                if row[8]==Inside the field
                    data[3][0]+=1
                data[3][1]+=1
            elif row[9]==Home garden or irregular
                if row[8]==Inside the field
                    data[4][0]+=1
                data[4][1]+=1
#print(data)
propdata={One crop abs(0.5-data[0][0]data[0][1]), Multiple crops abs(0.5-data[1][0]data[1][1]), Fallow abs(0.5-data[2][0]data[2][1]), Pasture abs(0.5-data[3][0]data[3][1]), Home garden abs(0.5-data[4][0]data[4][1])}
#print(propdata)

plt.bar(propdata.keys(), propdata.values(), color=green, width=0.5)
plt.ylabel(0.5 - Proportion of Inside the Field Points)
plt.show()