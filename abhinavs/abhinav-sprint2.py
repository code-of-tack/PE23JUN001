# Here is the final problem statement for Sprint 2
# You are part of a team developing an e-commerce platform called "ShopSmart." As part of this platform, you have been assigned the task of creating a feature that helps users find the second-largest price among a list of products. This feature will assist users in making informed purchasing decisions, comparing prices, and identifying the best deals available.

# To accomplish this, you decide to create a program that takes a list of integers as input, representing the prices of different products, and finds the second-largest number in the list. The program will provide users with the second-largest price, along with additional functionality to enhance their shopping experience.

# When a user visits the ShopSmart platform and selects the product browsing section, they will be presented with a list of products along with their prices. The program will display a message like:

# Welcome to ShopSmart Product Browsing!
# Here are the prices of the available products:
# [9.99, 14.99, 24.99, 19.99, 12.99, 29.99, 8.99]



# The user can then analyze the prices and identify the second-largest price among them.

# Upon identifying the second-largest price, the user can proceed with making a purchase decision, taking into consideration the price variation, product features, customer reviews, and other factors.

# solution




#defining a function that takes list as input and returns second largest elemnent as output
def second_max_element(numerical_data):
    #creating a copy of the given list so that  we do not disturb the original list
    numerical_data_copy=numerical_data
    #finding a the max element
    first_max=max(numerical_data_copy)
    #removing the first element
    numerical_data_copy.remove(first_max)
    #finding the next first elment i.e the second max element
    second_max=max(numerical_data_copy)
    #returning the second max element 
    return second_max


def main():
    print("""Welcome to ShopSmart Product Browsing!
    Here are the prices of the available products:""")
    #taking input of the list from the user
    numerical_data = list(map(float,input().split(",")))
    #printing  the second max element in the list
    print("The second largest price is: ", second_max_element(numerical_data))


# Run the program
if __name__ == '__main__':
    main()