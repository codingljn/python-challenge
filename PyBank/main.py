# Modules
import os
import csv

# #Set path for files
budgetCSV=os.path.join("budget_data.csv")
budgettxt=os.path.join("budget_data.txt")

# Open and read csv
with open(budgetCSV, newline="") as csvfile:
# Read and split the data by commas and put into string variable csvreader
    csvreader=csv.reader(csvfile,delimiter=",")
# Skip header row
    next(csvreader)
# Initial values
    months=0
    deltaProfit=[]
    tprofit=0
    deltaMonth=0
    avgChng=0
    totChng=0
# Convert csvreader from string to list 
    for line in csvreader:
        deltaProfit.append(line)
        tprofit+=int(line[1])
        months+=1           
# Define formulas for greatest increase and decrease
    grtIncr=int(deltaProfit[months-1][1])-int(deltaProfit[months-2][1])
    grtDecr=int(deltaProfit[months-1][1])-int(deltaProfit[months-2][1])    
# Calculation for profit gains/losses on a monthly basis
    for i in range(months,1,-1): # stops before header
        deltaMonth=int(deltaProfit[i-1][1])-int(deltaProfit[i-2][1])
        # Loop through values and find greatest increase and decrease
        if deltaMonth < grtDecr:
            minDate=deltaProfit[i-1][0]
            grtDecr=deltaMonth
        elif deltaMonth > grtIncr:
            grtIncr=deltaMonth
            maxDate=deltaProfit[i-1][0]
#Total change
    totChng=totChng+deltaMonth
#Average change   
    avgChng=totChng/(months-1)

# Print to console
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(months))
print("Total: $"+str(tprofit))
print("Average  Change: $"+str(round(avgChng,2)))
print("Greatest Increase in Profits: "+maxDate+" ($"+str(grtIncr)+")")
print("Greatest Decrease in Profits: "+minDate+" ($"+str(grtDecr)+")")

# Save output to a text file
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

text_file=open(budgettxt,"w")
text_file.write("Financial Analysis")
text_file.write("\n----------------------------")
text_file.write("\nTotal Months: "+str(months))
text_file.write("\nTotal: $"+str(tprofit))
text_file.write("\nAverage  Change: $"+str(round(avgChng,2)))
text_file.write("\nGreatest Increase in Profits: "+maxDate+" ($"+str(grtIncr)+")")
text_file.write("\nGreatest Decrease in Profits: "+minDate+" ($"+str(grtDecr)+")")
# Close file and free up system resources
text_file.close()