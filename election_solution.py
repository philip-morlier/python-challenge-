import csv
import os

pypoll_csv = os.path.join('election_data.csv')


mylist = []
with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for line in csvreader:
        mylist.append(line)

def total_votes(columns):
    sum = 0 
    for line in mylist:
        if 'Voter' not in line[0]:
            sum = sum + 1
    return sum

def khan_votes(columns):
    khan_sum = 0 
    for line in mylist:
        if 'Candidate' not in line[2] and 'Khan' in line[2]:
            khan_sum = khan_sum + 1
    return khan_sum

def correy_votes(columns):
        correy_sum = 0 
        for line in mylist:
            if 'Candidate' not in line[2] and 'Correy' in line[2]:
                correy_sum = correy_sum + 1
        return correy_sum