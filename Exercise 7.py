#You are part of a team developing a fitness tracking app called "FitTrack." As part of this app, you have been assigned the task of creating a feature that allows users to track their workout progress by recording and analyzing their lifting weights. One important aspect of weight tracking is the ability to identify the highest and lowest weights lifted during a workout session to monitor progress and set new goals.
#To accomplish this, you decide to create a program that takes a list of integers as input, representing the weights lifted during a workout session, and prints the largest and smallest numbers in the list. The program will provide users with the maximum and minimum weights lifted, along with additional functionality to enhance their fitness tracking experience.
#When a user opens the FitTrack app and selects the weight tracking feature, they will be prompted to enter the weights lifted during their workout session. The program will display a message like:
#Welcome to FitTrack Weight Tracking!
#Please enter the weights lifted during your workout session, separated by commas:
#The user can then input a list of weights, for example: 50, 65, 45, 70, 55.
#Upon receiving the input, the program will process the list of weights, identify the largest and smallest numbers, and display the result, saying:
#Thank you for providing your weight data.
#The largest weight lifted during your workout session was: 70 kg
#The smallest weight lifted during your workout session was: 45 kg

#My code 

print("Welcome to Fittrack Weight Tracking!") #initial print statement 
def find_max_min(numbers): #defining the function
    if not numbers:
        return None, None

    maximum = minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


# getting input from user 
num_list = input("Please enter the weights lifted during your workout session , separated by spaces: ").split()
num_list = list(map(int, num_list))

max_num, min_num = find_max_min(num_list) #finding the max and min values from the user list 
print("Thank you for providing your weight data.")
print("The largest weight lifted during your workout session was:{}".format(max_num))
print("The smallest weight lifted during your workout session was:{}".format(min_num))