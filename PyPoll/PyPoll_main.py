import os
import csv

election_csv=os.path.join("Resources", "election_data.csv")

Stockham_votes=0
DeGette_votes=0
Doane_votes=0
total_votes=[]

#Candidates=["Charles Casper Stockham", "Diana DeGette","Raymon Anthony Doane"]

#open csv file
with open(election_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
#skip header
    csv_header=next(csv_file)
#Create a list for total votes and append row 0 for the total

    for row in csv_reader:
        total_votes.append(row[0])
        

#Find total votes for each candidate with the below conditional


        if row[2] == "Charles Casper Stockham":
            Stockham_votes=Stockham_votes+1
        elif row[2]== "Diana DeGette":
            DeGette_votes=DeGette_votes+1
        elif row[2]== "Raymon Anthony Doane":
            Doane_votes=Doane_votes+1


#Find total candidate votes
total_candidate_votes=(Stockham_votes+DeGette_votes+Doane_votes)
            
Stockham_percent=round(((Stockham_votes/total_candidate_votes)*100),3)
DeGette_percent=round(((DeGette_votes/total_candidate_votes)*100),3)
Doane_percent=round(((Doane_votes/total_candidate_votes)*100),3)

#Print it all out
print("Election Results")
print("------------------------------------")
print(len(total_votes))
print("------------------------------------")
print(f"Charles Casper Stockham:",(Stockham_percent),((Stockham_votes)))
print(f"Diana DeGette:", (DeGette_percent) ,((DeGette_votes)))
print(f"Raymon Anthony Doana:", (Doane_percent), ((Doane_votes)))
print("-------------------------------------")

if(Stockham_votes>DeGette_votes)and(Stockham_votes>Doane_votes):
    print("Winner: Charles Casper Stockham")
elif(DeGette_votes>Stockham_votes)and(DeGette_votes>Doane_votes):
    print("Winner: Diana DeGette")
elif(Doane_votes>Stockham_votes)and(Doane_votes>DeGette_votes):
    print("Winner: Raymon Anthony Doane")
print("--------------------------------------")

file=open("PyPoll_Results.txt","w")
file.write("Election Analysis")
file.write("\n")
file.write("---------------------------------")
file.write("\n")
file.write(len(total_votes))
file.write("\n")
file.write("---------------------------------")
file.write(f"Charles Casper Stockham:",(Stockham_percent),((Stockham_votes)))
file.write(f"Diana DeGette:", (DeGette_percent) ,((DeGette_votes)))
file.write(f"Raymon Anthony Doana:", (Doane_percent), ((Doane_votes)))
file.write("----------------------------------")
file.write("Winner: Diana DeGette")