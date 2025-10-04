class parrot:
    speices = "birds"
    def __init__(self , name , age):
        self.name = name
        self.age = age
blue = parrot("blue" , 10)
woo = parrot("woo" , 7)
print("Blue is a {}".format(blue.speices)) 
print("Woo is a {}".format(woo.speices)) 
print("{} is {} years old ".format(blue.name , blue.age))
print("{} is {} years old ".format(woo.name , woo.age))