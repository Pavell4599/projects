class MyClass:
    def __init__(self):
        self.name = "Mys"

class_name_str = "MyClass"
my_object = globals()[class_name_str]()
print(my_object)
