start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

squares = [num ** 2 for num in range(start, end + 1)]
print("\nList of square values:", squares)

even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

print("\nEven square values:", even_squares)
print("Odd square values:", odd_squares)