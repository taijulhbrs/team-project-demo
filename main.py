import math

robot_name = input("What is your robot's name? ")
print("Hello, " + robot_name + "! Welcome to the world of robotics!")

# Creating a calculator with medium range of features
def calculator():
    print("Welcome to the Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (sqrt)")
    print("7. Factorial (!)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Exit")

    while True:
        try:
            choice = input("Enter the number of the operation you want to perform: ")
            if choice == "11":
                print("Goodbye!")
                break
            elif choice == "1":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 + num2
                print(f"The result is: {result}")
            elif choice == "2":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 - num2
                print(f"The result is: {result}")
            elif choice == "3":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 * num2
                print(f"The result is: {result}")
            elif choice == "4":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
                print(f"The result is: {result}")
            elif choice == "5":
                num1 = float(input("Enter the base number: "))
                num2 = float(input("Enter the exponent: "))
                result = num1 ** num2
                print(f"The result is: {result}")
            elif choice == "6":
                num = float(input("Enter the number: "))
                if num < 0:
                    print("Error: Square root of negative number!")
                    continue
                result = math.sqrt(num)
                print(f"The result is: {result}")
            elif choice == "7":
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Error: Factorial of negative number!")
                    continue
                result = math.factorial(num)
                print(f"The result is: {result}")
            elif choice == "8":
                angle = float(input("Enter the angle in degrees: "))
                result = math.sin(math.radians(angle))
                print(f"The result is: {result}")
            elif choice == "9":
                angle = float(input("Enter the angle in degrees: "))
                result = math.cos(math.radians(angle))
                print(f"The result is: {result}")
            elif choice == "10":
                angle = float(input("Enter the angle in degrees: "))
                result = math.tan(math.radians(angle))
                print(f"The result is: {result}")
            else:
                print("Invalid choice! Please select a valid operation.")
        except ValueError:
            print("Error: Invalid input! Please enter a number.")

# Call the calculator function
calculator()