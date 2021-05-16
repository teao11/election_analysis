''' ROCK PAPER SCISSORS EXAMPLE
import random as rd

userChoice = input("Rock (r), Paper (p) or Scissors (s): ")

compChoice = rd.randint(1,3)

if int(compChoice) == 1:
    compChoice = "r"
elif int(compChoice) == 2:
    compChoice = "p"
elif int(compChoice) == 3:
    compChoice = "s"

print(f'User chose {userChoice}')
print(f'Computer chose {compChoice}')
print()

if userChoice == compChoice:
    print("TIE!")
elif (userChoice == "r") and (compChoice == "s"):
    print("You win!")
elif (userChoice == "s") and (compChoice == "p"):
    print("You win!")
elif (userChoice == "p") and (compChoice == "r"):
    print("You win!")
else:
    print("You lose!") '''

#____________________________________________________________________________________________________________________________________

''' # NUMBER CHAIN EXERCISE
repeat = "y"

startNumber = int(input("Please choose a number to start from: "))

while repeat == "y":

    print(f'Starting at {startNumber}!')
    numberCount = int(input("Please choose how many numbers you would like to out: "))
    threshold = startNumber + numberCount

    while startNumber < threshold:

        print(startNumber)
        startNumber = startNumber + 1

    repeat = input("Would you like to restart? (y/n): ")

print("Beep bop boop exiting loop!") '''

''' #____________________________________________________________________________________________________________________________________

# IMPORT OS and use os.path.join()
# IMPORT csv --> with open(csvpath, newline='') as csvfile

# Modules
import os
import csv

# Set a variable to false to check if we found the video
found = False

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("Resources","Python_2_07-Stu_ReadNetFlixCSV_netflix_ratings.csv")

# Open the CSV
with open(csvpath, newline="") as file_handler:
    
    csvreader = csv.reader(file_handler, delimiter=",")
    print(csvreader)

    # Loop through looking for the video
    for row in csvreader:

        if(row[0]==video):
            
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            found = True

            break

    if found is False:

        print(f"Can't find {video}... Sorry about that!")

#____________________________________________________________________________________________________________________________________
 '''
