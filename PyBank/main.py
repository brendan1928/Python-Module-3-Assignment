#Importing modules

import os
import csv

netProfit = 0
greatestprofitInc = 0
greatestprofitDec = 0
rowCount = 0
prevRow = 0
changeSum = 0
profitChange = 0
pybank_csv = os.path.join('Resources','budget_data.csv') #Identifying path for our csv to be read from
results_txt = os.path.join('analysis','financial_results.txt') #Identifying path for our .txt to be created to

def average(total,count): #Simple average calculator
    average = total / count
    return average

def summarize_bank_data(rowCount, netProfit, changeSum, greatestprofitincDate,greatestprofitInc,greatestprofitdecDate,greatestprofitDec): #Reducing the denominator in the average function because we are measuring changes not rows 
    summary = f"Total Months: {(rowCount)} \n \
                Net Profit: ${netProfit} \n \
                Average Change: ${round(average(changeSum,(rowCount-1)),2)} \n \
                Greatest Increase in Profits: {greatestprofitincDate} ({greatestprofitInc}) \n \
                Greatest Decrease in Profits: {greatestprofitdecDate} ({greatestprofitDec})" #Function that returns summary, the string of summarized data
    print(summary) #Prints output in terminal
    return(summary) #Returns summary so we can reference it when building text file

with open(pybank_csv,encoding='UTF-8') as csvfile:
    #Splits data into commas
    csvreader = csv.reader(csvfile,delimiter=",")
    #Establishes first row as header
    header = next(csvreader)

    for row in csvreader:  
        rowCount +=1 #counts the row
        profitintValue = int(row[1]) #converts the profit or loss into an int
        if rowCount > 1: #does not calculate profit change on the first row and the header
            profitChange = profitintValue - prevRow  #calculates the change from the previous profit value
            print(profitChange)
        netProfit += profitintValue #tracks net profit over each row
        if profitChange > greatestprofitInc: #checks if profit change beats record high profit change
            greatestprofitInc = profitintValue
            greatestprofitincDate = row[0]
        elif profitChange < greatestprofitDec: #checks if profit change beats record low profit change
            greatestprofitDec = profitintValue
            greatestprofitdecDate = row[0]
        prevRow = profitintValue #sets the previous row to the value in row[1] / the profit
        changeSum += profitChange

with open(results_txt, 'w') as txtFile:
    txtFile.write(str(summarize_bank_data(pybank_csv)))





