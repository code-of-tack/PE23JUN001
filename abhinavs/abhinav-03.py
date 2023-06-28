# You are part of a team developing a financial planning application called "FinPlanPro." As part of this application, you have been assigned the task of creating a feature that generates the Fibonacci sequence up to a given number 'n'. This feature will assist financial planners and investment advisors in performing calculations related to interest rates, asset growth, and investment strategies.

# To accomplish this, you decide to create a Python program that generates the Fibonacci sequence up to a given number 'n'. The program will provide users with the Fibonacci sequence, along with additional functionality to enhance their financial planning capabilities.

# When a financial planner opens the FinPlanPro application and selects the Fibonacci generation feature, they will be prompted to enter the desired number 'n'. The program will display a message like:
# Welcome to FinPlanPro Fibonacci Generator!
# Please enter the desired number 'n' to generate the Fibonacci sequence:

# The financial planner can then input a number, for example: 100.

# Upon receiving the input, the program will generate the Fibonacci sequence up to the given number 'n' (in this case, 100). It will then display the result, saying:
# Thank you for providing the number 'n'.
# The Fibonacci sequence up to 100 is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89


#solution

#defining a function to create fibonacci series
def fibbo_series(n):
    
    a=0
    b=1
    
    #creating a list  to store answer
    list=[]
    
    #handling the exceptional case
    if(n==0):
        list.append(0)
    if(n==1):
        list.append(0)
        list.append(1)
        list.append(1)
            
    #writing the general code        
    if(n>1):
        list.append(0)
        list.append(1)
    while n>b:
        #storing the value to current elentent in a temp. variable
        temp=b
        #storing the new value of current elemnent
        b=a+b
        #storing the value stored in temp in earlier current element 
        a=temp
        #checking if the current element is less than or equal to n
        if(n>=b):
        #inserting the element in list
            list.append(b)
        #returning the list
    return list
    
    #defining the main function
def main():
    print("""Welcome to FinPlanPro Fibonacci Generator!
    Please enter the desired number 'n' to generate the Fibonacci sequence:""")
    
    #taking the input (n) from the user
    n=int(input())
    #printing the statement given in the question
    print("Thank you for providing the number ",n )
    #printing the list by calling the function fibbo_series
    print("The Fibonacci sequence up to 100 is:",fibbo_series(n))

# Run the program by calling the main ffunction
if __name__ == '__main__':
    main()