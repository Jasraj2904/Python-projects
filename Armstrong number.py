n = int(input("Enter your number : "))
sum = 0
temp = n 
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10
if (n == sum):
    print("It is an Amstrong Number")
else:
    print("It is not an Amstrong Number")