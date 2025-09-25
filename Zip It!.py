s1 = {2 , 3 , 1}
s2 = {'a' , 'd' , 'j'}
s3 = list(zip(s1 , s2))
print(s3)
list1 = [10 , 20 , 30  , 40]
list2 = [100 , 200 , 300 , 400]
for x,y in zip(list1 , list2[::-1]):
    print(x,y)
stoxs = ['reliance' , 'infosys' , 'TCS']
prices = [2000 , 3000 , 4000 ]
new_dictionary = {stoxs : prices for stoxs , prices in zip(stoxs , prices)}
print('\n{}'.format(new_dictionary))