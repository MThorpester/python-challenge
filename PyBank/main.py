# Import modules for os-independent functions and working with csv files 
import os
import csv

# Define the lists used to store the extracted data: Title, Price, Subscriber Count, Number of Reviews, and Course Length
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


# read through the budget_data.csv file - there are no headers and columns are:id, title, url, isPaid, price, numSubscribers, numReviews,
# numPublishedLectures, instructionalLevel, contentInfo, publishedTime
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

cwd = os.getcwd()
csvpath = os.path.join(cwd, 'Resources', 'budget_data.csv')

with open(csvpath, encoding="utf-8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    print(csvreader)
 
 # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
# store contents of the Month, Monthly Profits & Losses and Monthly Change in P&L into Python lists
# accumulate rolling counts & totals
 
    for row in csvreader:   
        months.append(row[0])
        profits_losses.append(int(row[1]))
        if total_months == 0:
            last_month_pl = int(row[1])
        change.append(int(row[1]) -last_month_pl)
        last_month_pl = int(row[1])
        total_months = total_months + 1
        total_profits_losses = (total_profits_losses + int(row[1]))
        total_change = total_change + change[-1]
        if change[-1] > greatest_increase_amt:
            greatest_increase_amt = change[-1]
            greatest_increase_month = (row[0])
        elif change[-1] < greatest_decrease_amt: 
            greatest_decrease_amt = change[-1]
            greatest_decrease_month = (row[0])
        

# compute the average change
average_change = total_change/total_months 

#Print the computed values to the terminal
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits_losses}")
print(f"Total Change: ${total_change}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase_amt}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease_amt}")



# Zip the lists together into a single tuple
zipped_pl = zip(months, profits_losses, change)


# save the output file path
output_file = os.path.join("MTZippedLists.csv")


# Write the contents of the extracted data into a CSV...make sure to include the titles of the columns
# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Months", "Profit & Loss", "Monthly Change"])

    writer.writerows(zipped_pl)