# dependencies
import csv
import os

# file paths
input_path=os.path.join("Resources","election_data.csv")
output_path=os.path.join("Analysis","election.analysis.txt")

# variables
vote_counter=0
candidate_names=[]
candidate_votes={}
winner=["",0]

# open and read the data
# with open("Resources/election_data.csv", "r") as data:
with open(input_path)as data:
    reader=csv.reader(data)
    header=next(reader)

    for row in reader:
        vote_counter+=1
        candidate_name=row[2]
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1





with open(output_path,"w")as file:
    voter_output=(
    f"""
Election Results
-------------------------
Total Votes: {vote_counter}
-------------------------
"""
)
    print(voter_output)   
    file.write(voter_output)

    for name in candidate_votes:
        votes=candidate_votes.get(name)
        vote_percent=votes/vote_counter * 100

        candidate_stats=f"{name}: {vote_percent:.3f}% ({votes})\n"
        print(candidate_stats)
        file.write(candidate_stats)

        if votes>winner[1]:
            winner[0]=name
            winner[1]=votes

    winner_output=(
        f"""
-------------------------
Winner: {winner[0]}
-------------------------


"""
    )
    print(winner_output)
    file.write(winner_output)

# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette