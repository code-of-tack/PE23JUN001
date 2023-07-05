#You are part of a team developing a text analysis tool called "TextInsight." As part of this tool, you have been assigned the task of creating a feature that allows users to analyze the frequency of characters in a given text. This feature will assist users in understanding the distribution of characters and identifying patterns within the text, which can be helpful for tasks such as language analysis, cryptography, or data validation.

#To accomplish this, you decide to create a program that takes a string as input and counts the number of occurrences of each character in the string. The program will provide users with a character frequency analysis, along with additional functionality to enhance their text analysis capabilities.
#When a user accesses the TextInsight tool and selects the character frequency analysis feature, they will be prompted to enter the text for analysis. The program will display a message like:
#Welcome to TextInsight Character Frequency Analysis!
#Please enter the text you would like to analyze:

#Mycode- 

print("Welcome to TextInsight Character Frequency Analysis!")
def count_characters(string): #defining a function
    char_count = {}
    
    # Counting the occurrences of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Printing the character count
    for char, count in char_count.items():
        print(f"{char}: {count}")
        
# Testing the function
input_string = input("Please enter the text you would like to analyze: ") # user input
print("Here is the character frequency analysis : ")
count_characters(input_string) #calling back function with value