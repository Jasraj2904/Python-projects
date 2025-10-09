class bird:
    def __init__(self):
        print("Bird is ready!")
    def who_is_this(self):
        print("Bird")
    def swim(self):
        print("Swim Faster.")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready!")
    def who_is_this(self):
        print("Penguin")
    def run(self):
        print("Run Faster.")
paggy = penguin()
paggy.who_is_this()
paggy.swim()
paggy.run()