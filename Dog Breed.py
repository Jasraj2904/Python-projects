class dog:
    speices = "Canis familiaris"
    def __init__(self , name ,  breed):
        self.name = name
        self.breed = breed
    def show_details(self):
        print(f"Name : {self.name} , Breed : {self.breed} , Speices : {self.speices}")
dog_1 = dog("Tommy" , "Labrador")
dog_2 = dog("Bruno" , "German Shepherd")

dog_1.show_details()
dog_2.show_details()