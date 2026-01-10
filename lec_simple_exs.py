class Number:
    def __init__(self, value):
        self.data = value


    def __add__(self, other):
        return Number(self.data + other)
    

a = Number(12)
c = Number(4)
b = a + 2
print(b.data)