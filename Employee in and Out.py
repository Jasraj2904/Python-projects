class employee:
    def __init__(self):
        print("Employee created.")
    def __del__(self):
        print("Destructor called.")
def create_object():
    print("Making object.")
    object = employee()
    print('function end')
    return object
object = create_object()
print("The program ends")