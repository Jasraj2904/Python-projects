Amount = int(input("Enter Your Amount = "))
Note1 = Amount//100
Note2 = (Amount%100)//50
Note3 = ((Amount%100) %50)//10
print("Notes of Rupee 100" , Note1)
print("Notes of Rupee 50" , Note2)
print("Notes of Rupee 10" , Note3)