# You are part of a team developing an online marketplace called "MarketSquare." As part of this marketplace, you have been assigned the task of creating a feature that allows sellers to manage their product listings effectively. One essential aspect of product management is sorting the product names in alphabetical order to ensure consistency and improve searchability for potential buyers.

# To accomplish this, you decide to create a Python program that takes a list of strings as input and sorts them in alphabetical order. The program will provide sellers with a sorted list of product names, along with additional functionality to enhance their product management capabilities.

# When a seller accesses the MarketSquare platform and navigates to the product management section, they will be presented with their existing product listings. The program will display a message like:

# Welcome to MarketSquare Product Management!
# Please enter your product names, separated by commas:


# The seller can then input a list of product names, for example: "Laptop, Smartphone, Headphones, Camera".

# Upon receiving the input, the program will process the list of product names, sort them in alphabetical order, and display the result, saying:

# Thank you for providing the product names.
# Here is the sorted list of product names:
# - Camera
# - Headphones
# - Laptop
# - Smartphone


# By sorting the product names alphabetically, MarketSquare ensures that sellers can easily locate and manage their products, and potential buyers can find products conveniently using search filters or browsing through categories.

#solution 
#defining the main fuction 
def main():    
    
    #asking for the input
    print("""Welcome to MarketSquare Product Management!
    Please enter your product names, separated by commas:""")
    
    #taking the input from the user in a list separated lby commas
    products_name = list(map(str,input().split(",")))
    #sorting the elments in the list using sort funtion 
    products_name.sort()
    #printing the list of products
    print("""Thank you for providing the product names.
    Here is the sorted list of product names:""")
    for i in products_name:
        print("- ",i)
        
        
# Run the program
if __name__ == '__main__':
    main()
        
        