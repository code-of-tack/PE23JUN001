#You are part of a team developing a mobile gaming app called "DiceMaster." As part of this app, you have been assigned the task of creating a feature that simulates a simple dice game, providing users with an entertaining experience while also allowing them to improve their mathematical skills.
#To accomplish this, you decide to create a Python program that simulates a simple dice game where the user rolls two dice, and the program prints the sum of the two numbers. The program will provide users with the sum, along with additional functionality to enhance their gaming experience.
#When a user opens the DiceMaster app and selects the dice game feature, they will be presented with a virtual dice rolling interface. The program will display a message like:
#Welcome to DiceMaster Dice Game!
#Press the 'Roll' button to roll the dice:
#The user can then tap the "Roll" button, simulating the roll of two dice. The program will generate random numbers for each dice, calculate the sum, and display the result, saying:
#Thank you for rolling the dice.
#You rolled a 3 and a 5. The sum is 8.

#MY code 

print("Welcome to DiceMaster Dice Game!") # Initial print statement 
import random #importing random function

def generate_random_number():
    return random.randint(1, 6)#initalising range from 1to6 as its a dice 

# Print "roll" and wait for user input
input("Press the 'ROLL' button to roll the dice and press enter:")#after pressing enter random numbers will be generated 

# Generate and print two random numbers
random_number1 = generate_random_number()#calling function for 1st value 
random_number2 = generate_random_number()#calling function for second value 
print("Thank you for rolling the dice.")

# Calculate and print the sum of the two numbers
sum_of_numbers = random_number1 + random_number2 # calculating sum of random genertaed values from above 
print("You rolled a {} and a {} . The sum is {}".format(random_number1,random_number2,sum_of_numbers))
