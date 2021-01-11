# python-challenge
This repo contains both the PyBank and PyPoll projects.

##**PyBank**
This project analyzes the financial records of a fictitious company. 
It consists of a Python script (main.py) that analyzes financial data stored in Resources\budget_data.csv, and outputs analysis results both to the terminal and to Analysis/Pybank_analysis.txt.
The input dataset is composed of two columns: Date and Profit/Losses. 
The Python script calculates and writes out:  
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

##**PyPoll**
This project helps a small (fictitious) rural town modernize its vote counting process.
It consists of a python script (main.py) that analyzes vote data stored in Resources\election_data.csv, and outputs analysis results both to the terminal and to Analysis/PyPoll_analysis.txt.
The input dataset contains Voter ID, County, and Candidate.
The script calculates and writes out:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.
