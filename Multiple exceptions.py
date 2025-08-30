try :
    num1 , num2 = eval(input("Enter 2 numbers seprated by comma : "))
    result = num1 / num2
    print("The result is : " , result ) 
except ZeroDivisionError :
    print("Divison by 0 is an error!! ")
except SyntaxError :
    print("Comma is missing!!")
except :
    print("Wrong Input!!")
else :
    print("No exceptions")
finally :
    print("This will execute no matter what!!")