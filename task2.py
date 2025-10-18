
class Pyramid:
    
    
    def __init__(self,max_h,bricks_count):
        
        self.max_h=max_h
        self.bricks_count=0
        
        self.now_height=0
        self.done=0
    
    
    def add_bricks(self):
        if self.now_layer%5==0:
           self.bricks_count+=5
        elif self.now_layer%5!=0:
           self.bricks_count+=5
           self.now_layer-=1 
           self.now_height+=1
        
        
    
    def get_height(self, now_height):
        self.bricks_count
    
    
    def is_done(self,done):
        
        self.done=(bricks_count/15)*100
        print(f"the pyramid is {done}% ready")
        
   

class Builder:
    
    
    def __init__(self, max_h):
        
        self.my_pyramid = Pyramid(max_h)
        self.number=0
        self.work_in_day=''
        self.bricks_need=0
        for i in range(1,max_h+1):
            self.bricks_need+=i
        self.now_layer=i
    
    
    
    def buy_bricks(self):
        self.a=i
        while a>0:
            self.a-=5
            self.number+=1
            self.bricks_count+=5
        
            
            
        self.bricks_count
   
    
    
    def build_pyramyd(self):
                       
    
    
    def work_day(self):
        if self.my_pyramid.self.now_height:
        
        
        
            
    
        
    
b = Builder(int(input()))

while True:
    b.work_day()        
