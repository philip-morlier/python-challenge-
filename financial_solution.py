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
        for line in banklist:
            if 'Profit/Losses' not in line[1]:
                sum = sum + int(line[1])
        return sum

def avr_change():
    
    curr=None
    prev=None
    
    for i,j in banklist:
        if j.startswith("P"):
            continue
        if prev is None:
            prev = int(j)
            continue
        
    curr = int(j)
    
    change = curr - prev
    
    for i,j in banklist:
        if j.startswith("P"):
            continue
        for i,j in banklist:
            sum = change 
        
    
    
    return sum / 85
        

def gre_inc():
        curr=None
        prev=None
        diff=None
        
        for i,j in banklist:
            if j.startswith("P"):
                continue
            if prev is None:
                prev = int(j)
                continue
            
            curr = int(j)
            
            if curr < prev:
                prev = curr
                continue
            
            currDiff = abs(curr - prev)
            if diff is None:
                diff = [i , currDiff]
            if currDiff > diff[1]:
                diff = [i , currDiff]
            
            prev = curr
        
        return diff

def gre_dec():
        curr=None
        prev=None
        diff=None
        
        for i,j in banklist:
            if j.startswith("P"):
                continue
            if prev is None:
                prev = int(j)
                continue
            
            curr = int(j)
            
            if curr > prev:
                prev = curr
                continue
            
            currDiff = curr - prev
            if diff is None:
                diff = [i , currDiff]
            if currDiff < diff[1]:
                diff = [i, currDiff]
            
            prev = curr
        
        return diff

 

        
            
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
        
def financial_results():
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months()}")
    print(f"Total: ${prolo_total()}")
    print(f"Average Change: ${round(avr_change(),2) }")
    print(f"Greatest Increase in Profits: {gre_inc()}")
    print(f"Greatest Decrease in Profits: {gre_dec()} ")

financial_results()


    
   