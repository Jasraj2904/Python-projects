class person(object):
    def __init__(self , name , IDnumber ):
        self.name = name
        self.IDnumber = IDnumber
    def display(self):
        print(self.name)
        print(self.IDnumber)
class employee(person):
    def __init__(self, name, IDnumber , salary , post):
        self.salary = salary
        self.post = post
        person.__init__(self , name , IDnumber)
a = employee('Rohan' , 7781 , 15000 , "In-tern")
a.display()