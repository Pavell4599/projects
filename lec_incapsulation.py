class Ball:
    def __init__(self):
        self.rad = 5 #public нужно \ можно
        self._name = 'pop' #private не нужно \ можно 
        self.__direct = 'Pavel' #protected не нужно \ нельзя


    #public метод
    
    def _update_radius(self, rad):
        self.rad = rad
        print('rad update to' + self.rad)


    #private метод
    def update_name(self, name):
        self._name = name
        print('name update to' + self._name)


    #protected метод
    def __update_direct(self, direct):
        print('111')


ball = Ball()
print(ball.rad)
print(ball._name)
#print(ball.__direct)
ball._Ball__update_direct(0)
