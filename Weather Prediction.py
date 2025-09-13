weather = ( 1 , 1 , 0 , 1 , 0 , 1)
sunny = 0
rainy = 0
for i in range(0 , 6):
    if (weather[i] == 0):
        sunny += 1
    else:
        rainy += 1
if(sunny > rainy):
    print("Good Weather")
else:
    print("Bad Wheather")