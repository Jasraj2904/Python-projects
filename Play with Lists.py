list_1 = [10 , 48 , 11 , 32 , 25]
print("Original List" , list_1)

sum = 0 

for i in list_1 :
    sum += i

print("The sum is : " , sum)

average = sum/len(list_1)
print("The average is : " , average)

list_1.sort()
print("The smallest element is : " , list_1[0])
print("The largest element is  : " , list_1[-1])