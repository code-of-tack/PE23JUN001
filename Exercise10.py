#You are part of a team developing an e-commerce platform called "ShopSmart." As part of this platform, you have been assigned the task of creating a feature that helps users find the second-largest price among a list of products. This feature will assist users in making informed purchasing decisions, comparing prices, and identifying the best deals available.
#To accomplish this, you decide to create a program that takes a list of integers as input, representing the prices of different products, and finds the second-largest number in the list. The program will provide users with the second-largest price, along with additional functionality to enhance their shopping experience.
#When a user visits the ShopSmart platform and selects the product browsing section, they will be presented with a list of products along with their prices. The program will display a message like:
#Welcome to ShopSmart Product Browsing!
#Here are the prices of the available products:
#[9.99, 14.99, 24.99, 19.99, 12.99, 29.99, 8.99]
#The user can then analyze the prices and identify the second-largest price among them.
#Upon identifying the second-largest price, the user can proceed with making a purchase decision, taking into consideration the price variation, product features, customer reviews, and other factors.


#mycode - 

print("Welcome to ShopSmart Product Browsing!")
def find_second_largest_number(series): #Function to find second large number 
    if len(series) < 2:
        return "Insufficient numbers to find the second largest."

    largest = max(series[0], series[1])
    second_largest = min(series[0], series[1])

    for number in series[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    return second_largest


def main():
    num_series = input("Here are the prices of the available products: ")
    series = [float(num) for num in num_series.split()]

    second_largest = find_second_largest_number(series)

    if isinstance(second_largest, str):
        print(second_largest)
    else:
        print("The second largest number is:", second_largest)


if _name_ == '_main_':
    main()

