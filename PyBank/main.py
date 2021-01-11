# Import modules for os-independent functions and working with csv files 
import os
import csv

# Define the lists used to store the extracted data: Months, Profits & Losses, Mnthly Change in P&L
months = []
profits_losses = []
change = []

# Define & initialize variables used for computations
last_month_pl = 0
total_months = 0
total_profits_losses = 0
total_change = 0  
greatest_increase_amt = 0
greatest_decrease_amt = 0

# open the budget_data.csv file
cwd = os.getcwd()
csvpath = os.path.join(cwd, 'Resources', 'budget_data.csv')

with open(csvpath, encoding="utf-8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
     
    # store the header row
    csv_header = next(csvreader)
      
    # store contents of the Month, Monthly Profits & Losses and Monthly Change into Python lists
    # accumulate rolling counts & totals
    for row in csvreader:   
        months.append(row[0])
        profits_losses.append(int(row[1]))
        # If it's the first row in the file, ensure that the monthly change that gets computed is zero 
        if total_months == 0:
            last_month_pl = int(row[1])
        # Compute the monthly change in p&l and append it to the monthly change list     
        change.append(int(row[1]) -last_month_pl)
        # set the last month's p&l variable to the current month's p&l to set up for when the next row gets processed 
        last_month_pl = int(row[1])
        # increment the total number of months processed
        total_months += 1
        # increment the total P&l variable
        total_profits_losses += int(row[1])
        # Add the current monthly change to the total change variable
        total_change += change[-1]
        if change[-1] > greatest_increase_amt:
            greatest_increase_amt = change[-1]
            greatest_increase_month = (row[0])
        elif change[-1] < greatest_decrease_amt: 
            greatest_decrease_amt = change[-1]
            greatest_decrease_month = (row[0])
    
# compute the average change
average_change = round(total_change/(total_months-1),2) 

#Print the analysis results to the terminal
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amt})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amt})")

# print the analysis results to a text file
cwd = os.getcwd()
txtpath = os.path.join(cwd, 'analysis', 'PyBank_analysis.txt')

with open(txtpath,"w") as txtfile:
    print("Financial Analysis", file=txtfile)
    print("-------------------------------------", file=txtfile)
    print(f"Total Months: {total_months}", file=txtfile)
    print(f"Total: ${total_profits_losses}", file=txtfile)
    print(f"Average Change: ${average_change}", file=txtfile)
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amt})", file=txtfile)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amt})", file=txtfile)

