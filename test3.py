class MyList:
        def __init__(self, data):
            self.data = data

        def print_items(self):
            # Перебор всех элементов списка
            for item in self.data:
                print(item)
my_list_object = MyList([1, 2, 3])
my_list_object.print_items()