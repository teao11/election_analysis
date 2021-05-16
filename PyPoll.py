import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

totalVotes = 0
candidateOptions = []
candidateVotes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load,'r') as election_data:

	# Read the file
	file_reader = csv.reader(election_data)

	# Print the header row
	headers = next(file_reader)
	print(headers)

	# Print each row in the CSV file
	for row in file_reader:

		totalVotes += 1
		candidate_name = row[2]

		if candidate_name not in candidateOptions:
			
			candidateOptions.append(candidate_name)
			candidateVotes[candidate_name] = 0

		candidateVotes[candidate_name] += 1

print(totalVotes)
print(candidateOptions)
print(candidateVotes)

for candidate_name in candidateVotes:

	votes = candidateVotes[candidate_name]
	vote_percentage = (float(votes)/float(totalVotes)) * 100
	print(f'{candidate_name}: received {vote_percentage: .1f}% ({votes:,}) of the total votes')

	if (votes > winning_count) and (vote_percentage > winning_percentage):

		winning_count = votes
		winning_percentage = vote_percentage
		winning_candidate = candidate_name

print(f'{winning_candidate} has won the election with {winning_count: ,} votes, or {winning_percentage: .1f}% of the votes')

