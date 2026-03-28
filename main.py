robot_name= input("What is your robot's name? ")
print("Hello, " + robot_name + "! Welcome to the world of robotics!")

#creating a new feature called calculator:
def calculator():
    print("Welcome to the calculator!")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print("The result is:", result)

# Call the calculator function
calculator()