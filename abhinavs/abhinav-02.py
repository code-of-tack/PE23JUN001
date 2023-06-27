# You are part of a team developing an AI-powered language learning platform called "LinguaTech." As part of this platform, you have been assigned the task of creating a feature that helps language learners analyze and improve their pronunciation skills by counting the number of vowels in a given sentence. This feature will assist learners in identifying vowel sounds, practicing their pronunciation, and achieving better fluency in the target language.

# To accomplish this, you decide to create a Python program that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in the sentence. The program will provide learners with valuable information about the vowel distribution, along with additional functionality to enhance their language learning experience.

# When a learner accesses the LinguaTech platform and selects the pronunciation analysis section, they will be prompted to enter a sentence they want to analyze. The program will display a message like:
# Welcome to LinguaTech Pronunciation Analyzer!
# Please enter a sentence to count the number of vowels:


# The learner can then input a sentence, for example: "The quick brown fox jumps over the lazy dog."

# Upon receiving the input, the program will process the sentence and count the number of vowels. It will then display the result, saying:
# Thank you for providing the sentence.
# The sentence "The quick brown fox jumps over the lazy dog." contains 11 vowels.






#solution 

#defining a function that counts the number of  vowels in a sentence
def number_of_vowels(sentence):
    
    
    #vowels
    vowel = set("aeiouAEIOU")
    
    #initiating counter
    count=0
    
    #traversing the sentence 
    for letter in sentence:
        
        #checking if the letter is present in the vowel
        if letter in vowel:
            count=count+1
    #returning the number of vowels
    return count
    
    
print("""Welcome to LinguaTech Pronunciation Analyzer!
Please enter a sentence to count the number of vowels:
    """)

#taking the input from the user
sentence=input()

#calling the function 
num_vowel=number_of_vowels(sentence)

#printing the final statement
print('the sentence "',sentence, '" contains ', num_vowel ," vowels.")