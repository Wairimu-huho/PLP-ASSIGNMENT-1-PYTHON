def calcutator():
    try:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        operator = input("Enter a mathematical operation(+, -, *, /):\n")
        
        if operator == '+':
            result = num1 + num2
            print(f"{num1} + {num1} = {result}")
            
        elif operator == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            
        elif operator == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            
        elif operator == '/':
            if num1 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                
            else:
                print("Error: Division by zero is not allowed.")
                
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        
calcutator()

