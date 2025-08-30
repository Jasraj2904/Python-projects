# Program to check if the entered age is correct and whether it is even or odd using try-except

try:
    age = int(input("Enter your age: "))

    # Check if age is within a valid range
    if 0 < age < 130:
        print(f"Valid age entered: {age}")

        # Check even or odd
        if age % 2 == 0:
            print("The age is Even.")
        else:
            print("The age is Odd.")
    else:
        print("Error: Age must be between 1 and 129.")

except ValueError:
    print("Error: Please enter a valid numeric age.")
