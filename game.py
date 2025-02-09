"""
Adventure Game - Tenebris
Author: Ethan Stiehr
Version: 1.0
Description:
Text base adventure game in the world Tenebris. Will you enter the machine?
"""

# Welcome message and introduction
print("Welcome to Tenebris!")  
print("Your eyes flutter open...")
print("Someone... No, something calls out to you.")

# Ask for the "abyss eater's" name
player_name = input("What is your name, abyss eater? ")

# Concatenate strings to create a personalized message
print("Greetings, " + player_name + ". Your path into darkness begins now.")

# Use an f-string to display the same message in a more readable way
print(f"Greetings, {player_name}. Your path into darkness begins now.")

# Intro to Tenebris
starting_area = """
You wake on a bridge between a thick forest and a large industrial wall.
Trees rustle on your left and large cogs turn in the wall on your right.
A door into the towering wall is seen across the way but a path to the forest has caught your eye first...
"""
print(starting_area)

# Decision 1
decision = input("Do you wish to take the path into the thick forest? (yes or no): ").lower()

# The response
if decision == "yes":
    print(f"Your choice has been made, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you take the door into the roaring industrial wall instead.")
else:
    print("The wall is deafining. The sounds are almost organic, you venture foward cautiously.")