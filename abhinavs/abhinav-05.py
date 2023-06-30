# Here is the Problem statement for June 30th
# You are part of a team developing a mobile gaming app called "DiceMaster." As part of this app, you have been assigned the task of creating a feature that simulates a simple dice game, providing users with an entertaining experience while also allowing them to improve their mathematical skills.

# To accomplish this, you decide to create a Python program that simulates a simple dice game where the user rolls two dice, and the program prints the sum of the two numbers. The program will provide users with the sum, along with additional functionality to enhance their gaming experience.

# When a user opens the DiceMaster app and selects the dice game feature, they will be presented with a virtual dice rolling interface. The program will display a message like:

# Welcome to DiceMaster Dice Game!
# Press the 'Roll' button to roll the dice:


# The user can then tap the "Roll" button, simulating the roll of two dice. The program will generate random numbers for each dice, calculate the sum, and display the result, saying:
# Thank you for rolling the dice.
# You rolled a 3 and a 5. The sum is 8.


# By simulating the dice game, DiceMaster provides users with a fun and interactive experience that combines chance and mathematical calculations. This feature is not only entertaining but can also be used as an educational tool to help users practice mental math and improve their arithmetic skills.

#solution
#importing random library
import random
#defining a function to roll a dice
def dice_roll():
    #using randint function from random number to generate a random number
    number=random.randint(1,6)
    #returning the gerenated nunber from the function call
    return number
    #defining the main function
def main():
    print("""Welcome to DiceMaster Dice Game!
    Press the 'Roll' button to roll the dice:""")
     
     #rolling 2 dices.
     #first roll
    dice1=dice_roll()
    #second roll
    dice2=dice_roll()
    
    
    print("Thank you for rolling the dice.")
    
    #printing the number on the rolled dice and there sum
    sum=dice1+dice2
    print("You rolled a",dice1,"and a", dice2,".The sum is", sum )

# Run the program
if __name__ == '__main__':
    main()