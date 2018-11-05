# Save output to a text file
# # https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

# Modules
import os
import csv

# #Set path for files
electionCSV=os.path.join("election_data.csv")
electiontxt=os.path.join("election_data.txt")

# Open and read csv
with open(electionCSV, newline="") as csvfile:
# Read and split the data by commas and put into string variable csvreader
    csvreader=csv.reader(csvfile,delimiter=",")
# Initial values
    votes=[]
    # Names of candidates
    dict_votes={}
# Number of votes
    elec_results={} 
# Skip header row
    next(csvreader)
    text_file=open(electiontxt,"w")
#Candidates will only print & write inside the loop (found out the hard way), so other console elements will be scattered throughout the code
    print("Election Results:")
    text_file.write("Election Results:")
    print("-------------------------")
    text_file.write("\n-------------------------\n")  
# Convert csvreader from string to list 
    for line in csvreader:
        votes.append(line)
    print("Total Votes: "+str(len(votes)))
    text_file.write("Total Votes: "+str(len(votes)))     
# Convert to dictionary
    for line in votes:
        name_key=line[2]
        if name_key not in dict_votes:
            dict_votes[name_key]=0
# Count names
        dict_votes[name_key]+=1
# Calculation for votes per candidate
total_votes=len(votes)
for name in dict_votes:
    elec_results[name]=round((dict_votes[name]/total_votes)*100)
    print(str(name)+": "+str(elec_results[name])+"% "+"("+str(dict_votes[name])+")")
    text_file.write("\n"+str(name)+": "+str(elec_results[name])+"% "+"("+str(dict_votes[name])+")")
# Most popular candidate
popular=0
# Find largest most popular candidate
for name in elec_results:
    if popular < elec_results[name]:
        popular=elec_results[name]
        winner=name
# This was printing multiple lines with the same info (56-59) when it was indented since it was inside the loop. I've moved it out so it prints only once.
print("-------------------------")
text_file.write("\n-------------------------")
print("Winner: "+winner)
text_file.write("\nWinner: "+winner)
# Close file and free up system resources
text_file.close()