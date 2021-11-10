# Programmer: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 11/4/21
# Lab Number: 7
# Program Inputs: The number of rolls of 2 dice
# Program Outputs: The total number between the 2 dice for every roll

# Import Random Library
import random
# Define function for number of rolls
def get_number_rolls():
    x = input("How many times do you want to role the die? ")
    if x.isdigit():
        return float(x)
    else:
        print("Invalid Input")
        get_number_rolls()
# Define function for rolling dice
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1+die2
# Define main function
def main():
    rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num = get_number_rolls()
    i = 0
    while i < num:
        x = roll_dice()
        rolls[x-2] += 1
        i += 1
    print(rolls)
    for i in rolls:
        print("*" * i)
main()