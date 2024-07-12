import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    
    # Prompt the user to input two numbers (when needed)
    num1 = float(input("Enter the first number: "))
    
    # Display the menu for operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    operation = input("Enter the number corresponding to the operation: ")
    
    if operation in ['1', '2', '3', '4', '5']:
        num2 = float(input("Enter the second number: "))
    
    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operation == '5':
        result = num1 ** num2
        print(f"The result of {num1} ^ {num2} is: {result}")
    elif operation == '6':
        if num1 >= 0:
            result = math.sqrt(num1)
            print(f"The square root of {num1} is: {result}")
        else:
            print("Error: Cannot take the square root of a negative number.")
    elif operation == '7':
        if num1 > 0:
            result = math.log(num1)
            print(f"The logarithm of {num1} is: {result}")
        else:
            print("Error: Logarithm is undefined for non-positive numbers.")
    elif operation == '8':
        result = math.sin(math.radians(num1))
        print(f"The sine of {num1} degrees is: {result}")
    elif operation == '9':
        result = math.cos(math.radians(num1))
        print(f"The cosine of {num1} degrees is: {result}")
    elif operation == '10':
        result = math.tan(math.radians(num1))
        print(f"The tangent of {num1} degrees is: {result}")
    else:
        print("Invalid operation choice. Please restart the calculator and choose a valid operation.")

# Run the scientific calculator function
scientific_calculator()

