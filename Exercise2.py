#You are part of a team developing an AI-powered language learning platform called "LinguaTech." As part of this platform, you have been assigned the task of creating a feature that helps language learners analyze and improve their pronunciation skills by counting the number of vowels in a given sentence. This feature will assist learners in identifying vowel sounds, practicing their pronunciation, and achieving better fluency in the target language.
#To accomplish this, you decide to create a Python program that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in the sentence. The program will provide learners with valuable information about the vowel distribution, along with additional functionality to enhance their language learning experience.
#When a learner accesses the LinguaTech platform and selects the pronunciation analysis section, they will be prompted to enter a sentence they want to analyze. The program will display a message like:
#Welcome to LinguaTech Pronunciation Analyzer!
#Please enter a sentence to count the number of vowels:

#Solution 

def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0 #initializing count to zero 
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count

print("Welcome to LinguaTech Pronounciation Analyzer!")
sentence = input("Please Enter a sentence to count the number of vowels: ")
vowel_count = count_vowels(sentence)
print(" Thank you for providing the sentence.")
print(" The sentence {} contains {} vowels".format(sentence,vowel_count))