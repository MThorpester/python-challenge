# Import modules for os-independent functions and working with csv files 
import os
import csv

# Define the lists used to store the extracted & computed data: candidates, candidate vote totals, 
# candidate vote percentage
candidates = []
votes = []
percentages = []

# Function to compute percentage of vote for a candidate
def compute_vote_percentage(candidate,vote, total):
    """ Returns win/loss statistics for election candidates. Arguments:candidate name, votes received, total number of votes """
    candidate_percentage = round((vote/total)*100)
    return(candidate_percentage)

# open the election_data.csv for reading
cwd = os.getcwd()
csvpath = os.path.join(cwd, 'Resources', 'election_data.csv')

with open(csvpath, encoding="utf-8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Skip the header row
    csv_header = next(csvreader)
 
# Read through election_data.csv, keeping a running tally of candidates and their vote totals
    total_votes = 0
    for row in csvreader:
        # If the candidate receiving the vote has already been added to the candidate list, increment their vote total 
        if row[2] in candidates:
            index = candidates.index(row[2])
            votes[index] = votes[index] + 1
        # If this is the first vote for this candidate, add them to the candidate list and add the vote to their vote total  
        else:
            candidates.append(row[2])
            votes.append(int(1))
        total_votes = total_votes + 1

max_votes = 0

# #Print the analysis results to the terminal
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
# Determine candidate vote percentages & the winner
# Print the results for each candidate to the terminal
for candidate in candidates:
    index = candidates.index(candidate)
    percentages.append(compute_vote_percentage(candidates[index],votes[index], total_votes))
    print(f'{candidates[index]}: {percentages[index]}% ({votes[index]})')
    if votes[index] > max_votes:
        winner = candidates[index]
        max_votes = votes[index]
# Print the rest of the analysis results to the terminal
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

# #print the analysis results to a text file
cwd = os.getcwd()
txtpath = os.path.join(cwd, 'analysis', 'PyPoll_analysis.txt')
with open(txtpath,"w") as txtfile:
    print("Election Results",file=txtfile)
    print("-------------------------------------",file=txtfile)
    print(f"Total Votes: {total_votes}",file=txtfile)
    print("-------------------------------------",file=txtfile)
    for candidate in candidates:
        index = candidates.index(candidate)
        print(f'{candidates[index]}: {percentages[index]}% ({votes[index]})',file=txtfile)
    
    print("-------------------------------------",file=txtfile)
    print(f"Winner: {winner}",file=txtfile)
    print("-------------------------------------",file=txtfile)

