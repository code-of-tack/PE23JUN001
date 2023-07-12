# You are part of a team developing a search engine called "SearchMaster." 
# As part of this search engine, you have been assigned the task of creating a feature 
# that finds the longest common prefix among a list of strings. 
# This feature will assist users in refining their search queries, improving search accuracy, 
# and providing relevant search suggestions based on the common patterns observed in previous search results.

# To accomplish this, you decide to create a program that finds the longest 
# common prefix among a list of strings. The program will provide users with the longest common prefix, 
# along with additional functionality to enhance their search experience.

# When a user accesses the SearchMaster website and enters a search query, the program will process the query and retrieve a list of related search results. 
# The program will then analyze the list of strings to find the longest common prefix. It will display a message like:

# Welcome to SearchMaster!
# Here are the search results related to your query:
# 1. "apple pie recipe"
# 2. "apple pie with cinnamon"
# 3. "apple pie filling"
# 4. "apple pie crust"


# The longest common prefix among these search results is: "apple pie"


# By identifying the longest common prefix among the search results, SearchMaster can offer search suggestions or refine the user's query to provide more accurate and relevant search results. This feature helps users save time and improves their overall search experience.
 
    
    
#solution

print("""Welcome to SearchMaster!
Here are the search results related to your query:
1. "apple pie recipe"
2. "apple pie with cinnamon"
3. "apple pie filling"
4. "apple pie crust""")
     

#defining the function
def longestCommonPrefix(strs):
    #lenght of a first element 
    l = len(strs[0])
    #checking for the common part in other elements 
    for i in range(1, len(strs)):
        #comparing the commom parts in the elements one by one 
        length = min(l, len(strs[i]))
        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            length = length - 1
            #returning the common part
            if length == 0:
                return 0
    return strs[0][0:length]

def main():
    #the input we could also make it like user have to enter it but for convinece i have taken in it a list
    strs = ["apple pie recipe","apple pie with cinnamon","apple pie filling", "apple pie crust"]
    #printing the common part by calling the longest common prefix
    print("The longest common prefix among these search results is:",longestCommonPrefix(strs))

# Run the program
if __name__ == '__main__':
    main()