#You are part of a team developing an advanced financial analytics platform for a leading investment firm called "QuantFinTech." As part of this platform, you have been assigned the task of creating a feature that allows investment analysts to quickly calculate the sum and average of a series of numerical data points. This feature will assist analysts in assessing the performance of investment portfolios, evaluating risk factors, and making informed investment decisions.
#To accomplish this, you decide to create a program that prompts the user to enter a series of numbers separated by spaces and then prints the sum and average of those numbers. The program will provide analysts with valuable statistical information, along with additional functionality to enhance their financial analysis capabilities.
#When an investment analyst opens the QuantFinTech platform and accesses the data analytics section, they will be presented with an input field and a message like:
#Welcome to QuantFinTech Data Analytics!
#Please enter a series of numerical data points separated by spaces:

# MY CODE 
numbers = []
print("Welcome to QuantFinTech Data Analytics!")
data = input("Please enter a series of numerical data points separated by spaces: ")
data_list = data.split()

for item in data_list:
    try:
        num = float(item)
        numbers.append(num)
    except ValueError:
        print(f"Ignoring non-numeric value: {item}")

sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

print("Sum:", sum_of_numbers)
print("Average:", average)