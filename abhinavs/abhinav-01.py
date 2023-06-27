# You are part of a team developing an advanced financial analytics platform for a leading investment firm called "QuantFinTech." As part of this platform, you have been assigned the task of creating a feature that allows investment analysts to quickly calculate the sum and average of a series of numerical data points. This feature will assist analysts in assessing the performance of investment portfolios, evaluating risk factors, and making informed investment decisions.

# To accomplish this, you decide to create a program that prompts the user to enter a series of numbers separated by spaces and then prints the sum and average of those numbers. The program will provide analysts with valuable statistical information, along with additional functionality to enhance their financial analysis capabilities.

# When an investment analyst opens the QuantFinTech platform and accesses the data analytics section, they will be presented with an input field and a message like:
# Welcome to QuantFinTech Data Analytics!
# Please enter a series of numerical data points separated by spaces:


# The analyst can then input the series of numbers, for example: "45.7 32.9 21.3 54.2 12.5".

# Upon receiving the input, the program will process the series of numbers and calculate the sum and average. It will then display the results, saying:
# Thank you for providing the data points.
# The sum of the numbers is: 166.6
# The average of the numbers is: 33.32



#solution
print("""Welcome to QuantFinTech Data Analytics!
Please enter a series of numerical data points separated by spaces:""")

#taking input from the user
numerical_data = list(map(float,input().split(" ")))

#calculating the sum
sum=0
for element in range(0,len(numerical_data)):
    sum=sum+numerical_data[element]

#calculating the average
average=(sum/len(numerical_data))

#printing the output
print("Thank you for providing the data points.")
print("The sum of the numbers is:",sum)
print("The average of the numbers is:",average)