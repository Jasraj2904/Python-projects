test_dict = {'Apple' : 2 , 'Banana' : 3 , 'Chery' : 2 , 'Guava' : 3 , 'Peach' : 1}

val = 3

freq = 0
for key in test_dict:
    if test_dict[key]== val:
        freq = freq + 1

print(f"The frequency of {val} is : " + str(freq) )