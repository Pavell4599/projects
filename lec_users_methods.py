class Ball:
    def __init__(self, mass):
        self.mass=mass
        self.image='hexagone'
        self.x=0
        self.y=0 
    def drop(self):
        print('Я подбросился')
        self.y+=2
    def kick(self):
        print('Я пнулся')
        self.x+=1
    def fail(self):
        self.mass=self.mass-0.1
    def printall(self):
        print(self.mass,
        self.image,
        self.x,
        self.y)
        
ball=Ball(0.5)
ball.drop()
ball.kick()
ball.fail()
print(ball.x)
print(ball.mass)
ball.printall()



ball.drop()
ball.kick()
ball.fail()
ball.fail()
ball.printall()


ball.drop()
ball.kick()
ball.fail()
ball.fail()
ball.printall()