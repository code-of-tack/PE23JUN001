#You are part of a team developing a social media platform called "RevShare." As part of this platform, you have been assigned the task of creating a feature that allows users to share and discover inspiring quotes. One essential aspect of quote sharing is the ability to present quotes in a visually appealing and engaging manner, including displaying quotes in reverse order to add a unique touch.
#To accomplish this, you decide to create a program that takes a string as input and prints the reverse of the string. The program will provide users with the reversed string, along with additional functionality to enhance their quote sharing experience.
#When a user accesses the RevShare platform and navigates to the quote sharing section, they will be prompted to enter their quote. The program will display a message like:
#Welcome to RevShare Quote Sharing!
#Please enter your quote:
#The user can then input their quote, for example: "Life is beautiful."
#Upon receiving the input, the program will process the quote, reverse the string, and display the result, saying:
#Thank you for sharing your quote.
#Here is your quote in reverse: "lufituaeb si efiL"

#My code -

print("Welcome to Revshare Quote Sharing!") #initial print statement
def reverse_string(string): #defining a function 
    reversed_string = string[::-1]
    return reversed_string

# Getting  user input
input_string = input("Please enter your quote: ")

# Calling the function and printing the reversed string
reversed_string = reverse_string(input_string)
print("Thank you for sharing your quote.")
print("Here is your quote in reverse:{}".format(reversed_string))