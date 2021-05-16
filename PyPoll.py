import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load,'r') as election_data:

	# Read the file
	file_reader = csv.reader(election_data)

	# Print the header row
	headers = next(file_reader)
	print(headers)

	