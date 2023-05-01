import os
import csv

budget_csv=os.path.join("Resources", "budget_data.csv")

#definitions sections
month_count=[]
Net_Total=[]
Profit_change=[]


#open csv file
with open(budget_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
#skip header
    csv_header=next(csv_file)

#circle through the csv with csv_reader. 
    for row in csv_reader:
        month_count.append(row[0])
#I tried many way to add the Profits with other functions but I found this easier just to make profits a list and append the data to it. 
        Net_Total.append(int(row[1]))
#Circle through the profits range to get the monthly change. You want to use a variable(x) to find the difference between two months, then append them to a list so you have 
#them for later. The -1 is used as a stopping place for the range.       
    for x in range(len(Net_Total)-1):
        Profit_change.append(Net_Total[x+1]-Net_Total[x])
#Python built in max and min functions to find maximum and minimum in our profit change list.
greatest_increase=max(Profit_change)
greatest_decrease=min(Profit_change)
#use the index function to find where in the profit change list the max and min are correlated. 
# The learning assistant helped me with the plus one, I kept getting the wrong month from the answer. Its because the profit change is associated with the next month.
greatest_increase_date=Profit_change.index(max(Profit_change))+1
greatest_decrease_date=Profit_change.index(min(Profit_change))+1

#Print statements, using 'f' function to allow embeded expressions
print("Financial Analysis")
print("--------------------------------------------------------------------")
#Len is included before month_count because with out it prints all the months in the list instead of the sum, and sum() doesnt work on lists
print(f"Total months: {len(month_count)}")
print(f"Total: ${sum(Net_Total)}")
# through online research I was able ot find this equation for average with two list. the round function was easy to understand, very similar to excel
print(f"Average change: , {round(sum(Profit_change)/len(Profit_change),2)}")
print(f"Greatest Increase in profits: {month_count[greatest_increase_date]} ({(greatest_increase)})")
print(f"Greatest Decrease in profits:  {month_count[greatest_decrease_date]} ({(greatest_decrease)})")

#write into text file:
file=open("Results.txt","w")
file.write("Financial Analysis")
file.write("\n")
file.write("-----------------------------------------------")
file.write("\n")
file.write(f"Total month: {len(month_count)}")
file.write("\n")
file.write(f"Average change: , {round(sum(Profit_change)/len(Profit_change),2)}")
file.write("\n")
file.write(f"Greatest Increase in profits: {month_count[greatest_increase_date]} ({(greatest_increase)})")
file.write("\n")
file.write(f"Greatest Decrease in profits:  {month_count[greatest_decrease_date]} ({(greatest_decrease)})")


