# Program to check if a character is an alphabet

# Input from user
char = input("Enter a character: ")

# Check if it's a single character
if len(char) != 1:
    print("Please enter only one character.")
else:
    # Check if it's an alphabet
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
