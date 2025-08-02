string = input("Please Enter Your Word : ")
char = input("Please Enter Your Characrter : ")

i = 0
count = 0

while ( i < len(string)):
    if (string [ i ] == char ) :
        count = count + 1
    i = i + 1

print(count, "The total number of times its repeats the character : ")