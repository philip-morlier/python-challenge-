import csv
import os

pybank_csv = os.path.join('budget_data.csv')

banklist = []

with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for line in csvreader:
        banklist.append(line)
    

def total_months():
    sum = 0 
    for line in banklist:
        if 'Date' not in line[0]:
            sum = sum + 1
    return sum


def prolo_total():
        sum = 0
        for row in banklist:
            if 'Profit/Losses' not in row[1]:
                sum = sum + int(row[1])
        return sum
        
            
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
        
def financial_results():
    print(total_months())
    print(prolo_total())

financial_results()


    
   