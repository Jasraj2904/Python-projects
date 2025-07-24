Medical_cause = input("Enter about Medical cuase Y or N = ")
atten = int(input("Enter your attendance percentage : "))

if (Medical_cause == 'Y'):
    print("You are allowed !")

else:
    if atten >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")