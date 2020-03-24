import os
import csv

# Define path to file
file = os.path.join("budget_data.csv")

# Setting initial values, to be changed in the for loop
months = 0
profLoss = 0
# Set increase/decrease to int, but the date to an empty string. 
greatInc = 0
incDate = ""
greatDec = 0
decDate = ""
last_row = 0
# To make finding the average easier, make the change a list. 
change = []

# Open the file, and separate the header from the rest of data
with open(file, "r") as data:
    budget = csv.reader(data, delimiter = ",")
    # Store the header in case we need it later
    header = next(budget)

    # Go through each row
    for row in budget:
        # Add to the total monthly count
        months = months + 1
        # Add to the total profit/loss
        profLoss = profLoss + int(row[1])
        # If the profit/loss is greater/lesser, reassign the values as necessary
        dif = int(row[1]) - last_row
        # Comparing the greatest increase to the current profit/loss
        if dif > greatInc:
            greatInc = dif
            incDate = row[0]
        # Comparing the greatest decrease to the current profit/loss
        if dif < greatDec:
            greatDec = dif
            decDate = row[0]
        # Need to exclude the first month because to accurately calculate the average later
        if months != 1:
            change.append(dif)
        # Store the current profit/loss as last_row for calculating the difference
        last_row = int(row[1])
    # Taking the sum of the values in the list "change", and the dividing by the number in the list. 
    avgchange = round(sum(change)/len(change),2)

# Saving the string as a variable to print and to export as text file.        
analysis = (f"""
Financial Analysis
-------------------------
Total Months: {months}
Total: ${profLoss}
Average Change: ${avgchange}
Greatest Increase in Profits: {incDate} ({greatInc})
Greatest Decrease in Profits: {decDate} ({greatDec})
""")

print(analysis)

# Specify the file name/type, and set it to a variable 
with open("analysis.txt", "w") as txt:
    txt.write(analysis)


