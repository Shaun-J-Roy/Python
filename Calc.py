def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Remainder")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print(num1, "/", num2, "=", num1 / num2)

        elif choice == '5':
            num = float(input("Enter the number to square: "))
            print(num, "^2 =", num ** 2)

        elif choice == '6':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print(num1, "%", num2, "=", num1 % num2)

        else:
            print("Invalid choice!")

calculator()
