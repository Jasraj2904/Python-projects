class io():
    def __init__(self):
        self.string1 = " "
    def get_string(self):
        self.string1 = input("Enter string.")
    def print_string(self):
        print("Result is " , self.string1.upper())
string1 = io()
string1.get_string()
string1.print_string()