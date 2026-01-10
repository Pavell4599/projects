class Number1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', other, self.val)
        return other + self.val


x = Number1(32)
y = Number1(25)

print(1 + x)
print(y + 3)


