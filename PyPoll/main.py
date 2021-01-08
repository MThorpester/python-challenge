# Import modules for os-independent functions and working with csv files 
import os
import csv

# Define the lists used to store the extracted data: candidates, candidate vote totals
candidates = []
votes = []
percentages = []
# =========================> stopped here

# Define & initialize variables used for computations


# read through the election_data.csv
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

cwd = os.getcwd()
csvpath = os.path.join(cwd, 'Resources', 'election_data.csv')

with open(csvpath, encoding="utf-8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    print(csvreader)
 
 # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
# Read through election_data.csv, keeping a running tally of candidates and their vote totals
    rowcount = 0
    for row in csvreader:
        rowcount = rowcount + 1
        if row[2] in candidates:
            index = candidates.index(row[2])
            votes[index] = votes[index] + 1
        else:
            candidates.append(row[2])
            votes.append(int(1))

print(f"Number of rows read: {rowcount}")    
print(candidates)
print(votes)

# Function and have it accept the 'wrestlerData' as its sole parameter

def compute_percentages(candidates,votes):
    """ Returns win/loss statistics for election candidates: candidate name, votes received, percentage of voteshare """
    for candidate in candidates:
        
    wins = int(wrestlerData[1])
    losses = int(wrestlerData[2])
    draws = int(wrestlerData[3])
    total_matches = wins + losses + draws
    pct_won = round((wins/total_matches)*100,2)
    pct_lost = round((losses/total_matches*100),2)
    pct_draws = round((draws/total_matches*100),2)

# #Print the computed values to the terminal
# print("Financial Analysis")
# print("-------------------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${total_profits_losses}")
# print(f"Total Change: ${total_change}")
# print(f"Average Change: ${average_change}")
# print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase_amt}")
# print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease_amt}")

# #print the computed values to a text file

# cwd = os.getcwd()
# txtpath = os.path.join(cwd, 'analysis', 'PyBank_analysis.txt')

# with open(txtpath,"w") as txtfile:
#     print("Financial Analysis", file=txtfile)
#     print("-------------------------------------", file=txtfile)
#     print(f"Total Months: {total_months}", file=txtfile)
#     print(f"Total: ${total_profits_losses}", file=txtfile)
#     print(f"Total Change: ${total_change}", file=txtfile)
#     print(f"Average Change: ${average_change}", file=txtfile)
#     print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase_amt}", file=txtfile)
#     print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease_amt}", file=txtfile)