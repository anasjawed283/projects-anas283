#simple calculator
  
#For adding two numbers 
def addition(n1, n2):
    return n1 + n2
  
#For substracting two numbers 
def subtraction(n1, n2):
    return n1 - n2
  
#For multiplying two numbers
def multiply(n1, n2):
    return n1 * n2
  
#For dividing two numbers
def divide(n1, n2):
    return n1 / n2
  
print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n")
  
  
#to take input from the user 
select = int(input("Choose assignment form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    addition(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtraction(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Plese enter a Valid operation number")