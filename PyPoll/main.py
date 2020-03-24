import os
import csv

# Defining a filepath
file = os.path.join("election_data.csv")

# Creating values that are equal to 0 outside the loop so there's something to add values in
totVote = 0
can1Vote = 0
can2Vote = 0
can3Vote = 0
can4Vote = 0
winner = ""
winVote = 0

# Create an empty list to figure out the names of the candidates
canList = []

with open(file, "r") as data:
    polling = csv.reader(data, delimiter = ",")

    # Save the header just in case
    header = next(polling)

    # Go through each row
    for row in polling:
        # Add to the total vote
        totVote += 1
        
        # Checking to see if the candidate name is in the list
        # If not, add it in
        if row[2] not in canList:
            canList.append(row[2])

        # Setting the first candidate's name to a value
        can1 = canList[0]

        # Since this goes line to line, need to check if there's a second value in the list
        # If so, assign the second name to a value
        if len(canList) == 2:
            can2 = canList[1]
        
        # Checking to see if there are 3 names, and assigning the third name
        if len(canList) == 3:
            can3 = canList[2]

        # Checking to see if there are 4 names, and assigning the fourth name
        if len(canList) == 4:
            can4 = canList[3]

        # If the candidate name = a value, add to their count
        if row[2] == can1:
            can1Vote += 1
        elif row[2] == can2:
            can2Vote += 1
        elif row[2] == can3:
            can3Vote += 1
        elif row[2] == can4:
            can4Vote += 1

# Calculating the percent of votes each candidate received
perc1 = round((can1Vote / totVote)*100,3)     
perc2 = round((can2Vote / totVote)*100,3)
perc3 = round((can3Vote / totVote)*100,3)
perc4 = round((can4Vote / totVote)*100,3)

# Comparing each candidate's vote to a variable called "winVote"
# If it is larger than "winVote", "winVote" changes to the value of that candidate's vote count
# "winner" then becomes the candidate name
if can1Vote > winVote:
    winner = can1
    winVote = can1Vote
elif can2Vote > winVote:
    winner = can2
    winVote = can2Vote
elif can3Vote > winVote:
    winner = can3
    winVote = can3Vote
elif can4Vote > winVote:
    winner = can4
    winVote = can4Vote

# Save results to a variable
analysis = (f"""
Election Results
-----------------------
Total Votes: {totVote}
-----------------------
{can1}: {perc1}% ({can1Vote})
{can2}: {perc2}% ({can2Vote})
{can3}: {perc3}% ({can3Vote})
{can4}: {perc4}% ({can4Vote})
-----------------------
Winner: {winner}
-----------------------
""")

# Print the variable to the terminal
print(analysis)

# Create a text document
with open ("analysis.txt", "w") as txt:
    txt.write(analysis)
