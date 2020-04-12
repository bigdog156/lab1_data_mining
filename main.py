import re
import enum
from dicTitle import *
#List title in dataset
ListTitle = []
ListData = []
Dict = {}

def processStringtoNumeric( text):
    return float(text)

def processFileData(file):
    data = open(file,'r')
    i = 0;
    for x in data:
        if i ==0:
            title = x[0:len(x)-1]
            title = re.split(',',title)
            ListTitle = title
            print(title)
            for item in title:
                Dict[item] = i
                i = i + 1
            print(Dict)
            
        else:
            title = x[0:len(x)-1]
            title = re.split(',',title)
            ListData.append(title)
    print(ListData)

    # Process dataset 
    data = ListData[0][1]
    print(data)
    dataDict = ListData[0][Dict['jod']]
    print(dataDict)
            


        

processFileData('test.txt')