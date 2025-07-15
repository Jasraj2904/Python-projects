import math

num = float(input("Enter a number to find the Square Root"))

if num < 0:
    print("Square Root of a negative number is not real")
else:
    sq = math.sqrt(num)
    print("The square root of", num, "is", sq)    