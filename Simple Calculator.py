print("\n==============================")
print("      SIMPLE CALCULATOR")
print("==============================")

print("Made by Veerendra Kalyan Babu")

while True:

    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            result = num1 + num2
            print(f"\n Result: {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\n Result: {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\n Result: {result}")

        elif choice == "4":

            if num2 != 0:
                result = num1 / num2
                print(f"\n Result: {result}")

            else:
                print("\n Cannot divide by zero")

        else:
            print("\n Invalid Choice")

    except ValueError:
        print("\n Please enter valid numbers")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("\n Thank you for using calculator")
        break