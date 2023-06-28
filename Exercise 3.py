#You are part of a team developing a financial planning application called "FinPlanPro." As part of this application, you have been assigned the task of creating a feature that generates the Fibonacci sequence up to a given number 'n'. This feature will assist financial planners and investment advisors in performing calculations related to interest rates, asset growth, and investment strategies.
#To accomplish this, you decide to create a Python program that generates the Fibonacci sequence up to a given number 'n'. The program will provide users with the Fibonacci sequence, along with additional functionality to enhance their financial planning capabilities.
#When a financial planner opens the FinPlanPro application and selects the Fibonacci generation feature, they will be prompted to enter the desired number 'n'. The program will display a message like:
#Welcome to FinPlanPro Fibonacci Generator!
#Please enter the desired number 'n' to generate the Fibonacci sequence:

#Solution 

# Program to display the Fibonacci sequence up to n-th term
#function to provide fibonaaci sequence 
def fibonacci(n):
    fib_sequence = [] #initializing the function 
    a, b = 0, 1 #variable assigned to start valuess 

    for _ in range(n): #loop through each value in range 
        fib_sequence.append(a) #appending the initial value for value greater than the initial value range 
        a, b = b, a + b

    return fib_sequence #returning back the call value 

print("Welcome to FinPlanPro Fibonacci Generator!")
n = int(input("please enter the desired number 'n' to generate the fibonacci sequence: ")) #desired input from the user 


fibonacci_sequence = fibonacci(n) #calling back the function to start the program 
print("Thank you for providing the number {}".format(n))#Display the result after the user has enterd the data 
print("The fibonacci sequence up to {} is {}".format(n,fibonacci_sequence))#final call and print statemnt 