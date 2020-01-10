import csv
import os

pypoll_csv = os.path.join('election_data.csv')


mylist = []


with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for line in csvreader:
        mylist.append(line)


def total_votes():
    sum = 0 
    for line in mylist:
        if 'Voter' not in line[0]:
            sum = sum + 1
    return sum

def khan_votes():
    khan_sum = 0 
    for line in mylist:
        if 'Candidate' not in line[2] and 'Khan' in line[2]:
            khan_sum = khan_sum + 1
    return khan_sum

def correy_votes():
        correy_sum = 0 
        for line in mylist:
            if 'Candidate' not in line[2] and 'Correy' in line[2]:
                correy_sum = correy_sum + 1
        return correy_sum

def tool_votes():
        tool_sum = 0 
        for line in mylist:
            if 'Candidate' not in line[2] and 'O' in line[2]:
                tool_sum = tool_sum + 1
        return tool_sum

def li_votes():
        li_sum = 0 
        for line in mylist:
            if 'Candidate' not in line[2] and 'Li' in line[2]:
                li_sum = li_sum + 1
        return li_sum

khan = khan_votes()
correy = correy_votes()
tool = tool_votes()
li = li_votes()

vote_count = [khan, correy, tool, li]

def winner():
    
    if khan is max(vote_count):
        return "Winner: Khan"
    elif correy is max(vote_count):
        return "Winner: Correy"
    elif tool is max(vote_count):
        return "Winner: O'Tooley"
    elif li  is max(vote_count):
        return "Winner: Li"
    else:
        raise Exception('Nobody Wins')


def election_results():
  	t_v = total_votes()
  	print("Election Results" )
  	print("--------------------")
  	print(f"Total Votes: {t_v}")
  	print("--------------------")
  	print(f"Khan: {round(khan_votes()  / t_v ,2) * 100}% ({khan_votes()})")
  	print(f"Correy: {round(correy_votes() / t_v ,2) * 100}% ({correy_votes()})")
  	print(f"O'Tooley: {round(tool_votes() / t_v ,2) * 100}% ({tool_votes()})")
  	print("Li: %.1f%% (%d)" % ((li_votes() / t_v) * 100, li_votes()))
  	print("--------------------")
  	print(f"{winner()}")
  	print("--------------------")

election_results()

exp_file = open("export_test0.txt", "+w")

