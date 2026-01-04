class MyClass:
    counts = 0
    
    def __init__(self):
        MyClass.counts = MyClass.counts + 1
        
    @classmethod 
    def ex_count(cls): #cls как self для classmethod
        print(cls.counts)
        
MyClass.ex_count()
m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

MyClass.ex_count()
m1.ex_count()