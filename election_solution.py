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

def tool_votes(columns):
        tool_sum = 0 
        for line in mylist:
            if 'Candidate' not in line[2] and 'O' in line[2]:
                tool_sum = tool_sum + 1
        return tool_sum

def li_votes(columns):
        li_sum = 0 
        for line in mylist:
            if 'Candidate' not in line[2] and 'Li' in line[2]:
                li_sum = li_sum + 1
        return li_sum

khan = khan_votes(mylist)
correy = correy_votes(mylist)
tool = tool_votes(mylist)
li = li_votes(mylist)

vote_count = [khan, correy, tool, li]

def winner():
    
    if khan is max(vote_count):
        return "Khan wins"
    elif correy is max(vote_count):
        return "Correy wins"
    elif tool is max(vote_count):
        return "O'Tool wins"
    elif li is max(vote_count):
        return "Li wins"
    else:
        raise Exception('Nobody Wins')