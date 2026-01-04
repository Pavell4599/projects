class SummatorClass:
    @staticmethod 
    def sum_1(a, b):
        print(a + b)
        
    def sum_2(self, a, b):
        print(a + b)
        
    def sum_3(self, a, b):
        return SummatorClass.sum_1(a, b)
    
SummatorClass.sum_1(5, 10)

sum_num = SummatorClass()
sum_num.sum_1(10, 15)
sum_num.sum_2(20, 25)
