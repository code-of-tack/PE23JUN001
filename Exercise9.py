#You are part of a team developing a language learning platform called "WordMaster." As part of this platform, you have been assigned the task of creating a feature that allows users to analyze and understand the complexity of different texts by counting the number of words in a given file. This feature will assist users in improving their vocabulary, assessing text difficulty, and tracking their reading progress.
#To accomplish this, you decide to create a program that reads a file and counts the number of words in the file. The program will provide users with the word count, along with additional functionality to enhance their text analysis capabilities.
#When a user accesses the WordMaster platform and selects the word count feature, they will be prompted to provide the path to the file they want to analyze. The program will display a message like:
#Welcome to WordMaster Word Count Analysis!
#Please enter the path to the file you want to analyze:
#The user can then input the file path, for example: path/to/myfile.txt.
#Upon receiving the input, the program will read the file, count the number of words, and display the result, saying:
#Thank you for providing the file for analysis.
#The file contains 526 words.


#Mycode -
print("Welcome to WordMaster Word Count Analysis!")
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print("File not found.")
        return -1

# Example usage
file_path = input("Please enter the path to the file you want to analyze: ")
word_count = count_words(file_path)
print("Thank you for providing the file for analysis.")
if word_count >= 0:
    print("The file contains {} words".format(word_count))