# Get input from the user
number = input("Enter a number: ")

# Remove negative sign or decimal point if present
filtered_number = number.replace("-", "").replace(".", "")

# Count the number of digits
digit_count = len(filtered_number)

# Display the result
print("Total digits in the number:", digit_count)
