# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total # of votes each candidate won
# 5. The winner of the election based on popular vote


#add our dependencies. 
import csv
import os

#Assign a variable to laod a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter. 
total_votes = 0

# Candidate Options
candidate_options = []

#Declare a dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file. 
with open(file_to_load) as election_data:

    #To do: read and analyze data here
    #Read the file object with reader function. 
    file_reader = csv.reader(election_data)

    #Read and print the header row. 
    headers = next(file_reader)
    
    #Print each row in the CSV file. 
    for row in file_reader:
        #Add to the total vote count. 
        total_votes += 1

        #Print the candidate name from each row. 
        candidate_name = row[2]

        #If the candidate does not match any existing candidate. 
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates. 
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count. 
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1

#Save the results to our text file. 
with open(file_to_save, "w") as txt_file: 
    #Print the final vote count to the terminal. 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file. 
    txt_file.write(election_results)

    for candidate_name in candidate_votes: 
        #Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print the candidate name & percentage of vots. 
        #Print each candidates voter count & % to terminal. 
        print(candidate_results)
        #Save the results to our text file. 
        txt_file.write(candidate_results)
     

        #Determine winning vote count & candidate
        #Determine if the votes is greater than winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            #If true then set winning_count = votes & winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_cand equal to the candidate's name. 
            winning_candidate = candidate_name

        #To do: print out winning candidate, vote count, and percentage. 
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    #Save winning results to text file. 
    txt_file.write(winning_candidate_summary)
    


