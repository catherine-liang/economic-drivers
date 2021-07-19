import matplotlib.pyplot as plt
import pandas as pd
import time
import csv
import numpy as np


#source: https://www.bls.gov/cew/downloadable-data-files.htm

start = time.time()
yearstart = 2010
yearend = 2016
worklist = []
currentlist =[]
found = 0
inflation = [1,1.04169609, 1.05902984,1.07760964,1.09994139, 1.10130280, 1.11228639]

for i in range(yearstart, yearend+1, 1):                                                        #for each year load in income data for total and private, county level, 
    
    year = i-2000
    inflat = inflation[i-yearstart]                                                                                   #formatting
    filepath = "./incomedata/"+str(i)+"_all_county_high_level"+"/allhlcn"+str(year)+".xlsx"         #the name of the file to reference
    print(filepath)
    current = pd.read_excel(filepath)                                                               #load current sheet
    print(current.head())
    temp = current.loc[current["Area Type"] == "County"]                                            #by county
    print(temp.head())
    temp2 = temp.loc[temp["Ownership"]=="Total Covered"]                                            #first looking at total covered 
    temp3 = temp2.loc[temp2["Industry"]=="Total, all industries"]                                   #by industry
    print(temp3["Area\nCode"].head())
    temp4 = temp3["Area\nCode"].tolist()
    #print(temp3["Area"].shape)
    if i == yearstart:
        worklist.append(temp3["Area\nCode"].tolist())                                                                            #create 2010 places as vertical headings
        worklist.append(temp3["Area"].tolist())
        # for j in range(len(worklist[0])):
        #     #print(j)
        #     condition = temp3["Area"] == worklist[0][j]
        #     indices = temp3.index[condition].tolist()
        #     currentlist.append(temp3.values[j][12])                                                  #12 is the annual avg pay column (i hope)
        worklist.append(temp3["Annual Average Pay"].tolist())            

    else:
        print("year = " + str(i))
        for j in range(len(worklist[0])):   #in the 2010 years, find the one in the current year
            #print(worklist[0][j]) ##############working until here
            # condition = temp3["Area"] == worklist[0][j]
            # indices = temp3.index[condition].tolist()
            # currentlist.append(temp3.values[j][12])
            for k in range(temp3["Area\nCode"].shape[0]):
                #if str(temp3.values[k][4]) == str(worklist[0][j]):
                #if k%100 ==0:
                    #print(str(temp4[k]) + "    " + str(worklist[0][j]))
                if int(temp4[k]) == int(worklist[0][j]):
                    #print("found " + "---------------------------")
                    currentlist.append(temp3.values[k][17]/inflat)
                    found+=1
                else:
                    #print("not found")
                    continue
        worklist.append(currentlist)
    

    #averageinc = temp3["Annual Average Pay"]
    #currentlist.append(averageinc)
    #print(currentlist[0])
    print(i)
    currentlist = []
    print(found)
    found =0

df = pd.DataFrame(worklist)
outfilepath = "incomedata.csv"

df.to_csv(outfilepath)

end = time.time()
print(end-start)







