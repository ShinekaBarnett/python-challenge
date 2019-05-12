import os 
import csv

#Create CSV Path
csvpath = os.path.join('PyBank','budget_data.csv')

#Create Variables
title = 'Financial Analysis'
dash = '-' * 25
totalMonths = 0
totalProfits = 0 
greatestIncrease = 0
greatestDecrease = 0 




#Read CSV File
with open(csvpath, newline='', encoding='utf-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")   
     csvheader = next(csvfile)
     
     for row in csvreader:
          #get total months
          totalMonths = totalMonths + 1
          #total profits
          totalProfits = totalProfits + int(row[1])
          


with open(csvpath, newline='', encoding='utf-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")   
     csvheader = next(csvfile)

     profitDiff = []      
     dataList = [row for row in csvreader]
     for i in range(0, totalMonths):
          if i > 0:
               profitDiff.append(float(dataList[i][1])- float(dataList[i-1][1]))
    
     profitAverage= sum(profitDiff)/len(profitDiff)

greatestIncrease=max(profitDiff)
greatestIncrease=profitDiff.index(max(profitDiff))
monthGreatestIncrease=dataList[greatestIncrease+1][0]


greatestDecrease=min(profitDiff)
greatestDecrease=profitDiff.index(min(profitDiff))
monthGreatestDecrease=dataList[greatestDecrease+1][0]



results =f"{title}\n{dash}\nTotal Months: {str(totalMonths)}\nTotal: ${totalProfits} \nAverage Change: ${profitAverage} \nGreatest Increase in Profits: {monthGreatestIncrease} (${greatestIncrease}) \nGreatest Decrease in Profits: {monthGreatestDecrease} (${greatestDecrease})"


print(results)
print
