import os
import csv

poll_csv = os.path.join('Resources','election_data.csv') #Initializing the csv path
results_txt = os.path.join('analysis','poll_results.txt') #Identifying path to create txt file to
#Declaring variables
votes = 0 
charles_votes = 0
charles_percentage = 0
diana_votes = 0
diana_percentage = 0
raymon_votes = 0
raymon_percentage = 0

#This function summarizes the vote results based on data obtained in the csvreader
def election_summary(poll_data):
    charles_percentage = (charles_votes / votes) * 100 #calculating the votes as a percentage
    diana_percentage = (diana_votes / votes) * 100
    raymon_percentage = (raymon_votes / votes) * 100
    
    #Rounding percentages to 3 decimal places based on prompt
    summarized_text = f"Election Results \n ------------------------------ \
        \n Total Votes: {votes} \n ------------------------------ \
        \n Charles Casper Stockham: {round(charles_percentage,3)}% ({charles_votes}) \
        \n Diana DeGette: {round(diana_percentage,3)}% ({diana_votes}) \
        \n Raymon Anthony Doane: {round(raymon_percentage,3)}% ({raymon_votes}) \
        \n ------------------------------ \n"
    if max(charles_votes,diana_votes,raymon_votes) == charles_votes:
        winner = "Winner: Charles Casper Stockham \n ------------------------------"
    elif max(charles_votes,diana_votes,raymon_votes) == diana_votes:
        winner = "Winner: Diana DeGette \n ------------------------------"
    elif max(charles_votes,diana_votes,raymon_votes) == raymon_votes:
        winner = "Winner: Raymon Anthony Doane \n ------------------------------"
    summarized_text += winner
    print(summarized_text)
    return summarized_text

#This loops through each row in the CSV and collects voting data
with open(poll_csv, 'r') as csvfile: #Opens CSV file as read-only
    csvreader = csv.reader(csvfile) #Do not need to put delimiter = ',' as this is the default
    header = next(csvreader)

    for row in csvreader: #loops through each row and counts the votes
        votes += 1
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes +=1

    election_summary(poll_csv) #Calls the summarizer function with the csv data

with open(results_txt, 'w') as txtFile:
    txtFile.write(election_summary(poll_csv))
    
