num = int(input("Enter Your NUmber : "))
temp = num
numlen = 0

while temp > 0 :
    numlen = numlen + 1
    temp = int( temp / 10 )

if numlen >= 4 :
    numlen = int( numlen / 2 ) 
    chk = 0
    while num > 0 :
        rem = num % 10
        if chk == numlen :
            midOne = rem
        elif chk == ( numlen - 1 ) :
            midTwo = rem
        num = int( num / 10 )
        chk = chk + 1
product = midOne * midTwo

print( product )