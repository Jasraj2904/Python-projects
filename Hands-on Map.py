a = [1 , 2 , 3]
b = [4 , 5 , 6]
result = map(lambda x ,y : x + y , a , b)
print("Addition of Two List")
print(list(result))
nums = [7 , 8 , 9 , 10 , 11]
def sq(n):
    return(n*n)
square = list(map(sq , nums))
print(square)