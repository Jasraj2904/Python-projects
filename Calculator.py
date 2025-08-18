def add(P,Q):
    return(P + Q)
def sub(P,Q):
    return(P - Q)
def multiply(P,Q):
    return(P * Q)
def divide(P,Q):
    return(P / Q)

print("Please select the opertion : ")
print("a. add" )
print("b. subtract" )
print("c. multiply" )
print("d. divide" )

choice = input("Please enter your choice of operation : ")
num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

if choice == 'a':
    print(add(num1 , num2))
elif choice == 'b':
    print(sub(num1 , num2))
elif choice == 'c':
    print(multiply(num1 , num2))
elif choice == 'd':
    print(divide(num1 , num2))