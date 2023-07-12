#You are part of a team developing an online marketplace called "MarketSquare." As part of this marketplace, you have been assigned the task of creating a feature that allows sellers to manage their product listings effectively. One essential aspect of product management is sorting the product names in alphabetical order to ensure consistency and improve searchability for potential buyers.
#To accomplish this, you decide to create a Python program that takes a list of strings as input and sorts them in alphabetical order. The program will provide sellers with a sorted list of product names, along with additional functionality to enhance their product management capabilities.
#When a seller accesses the MarketSquare platform and navigates to the product management section, they will be presented with their existing product listings. The program will display a message like:
#Welcome to MarketSquare Product Management!
#Please enter your product names, separated by commas:

#Program to print sorted list in alphabetical order 

print("Welcome to MarketSquare Product management!")#Initial print statement displayed to user 
words = input("please Enter your product names  separated by commas: ") #taking input from user 
word_list = [word.strip() for word in words.split(",")] #spliting the list in order make it easy for sorting
sorted_words = sorted(word_list) #sorting list in alphabetical order 
print("Thank you for providing the product names.")#returning output 
print("Here is the sorted list of product names :")
for word in sorted_words:
    print(word)#calling back the sorted value 