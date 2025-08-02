# Manual method to convert decimal to binary

decimal = int(input("Enter a decimal number: "))
binary = ""

# Repeat division by 2
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print("Binary equivalent:", binary)