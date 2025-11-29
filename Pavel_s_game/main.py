from player import *
from castle import *
from hero import *




if __name__ == '__main__':
    player1 = Player('red', 'Pavel_Legendaren')
    castle1 = Castle(player1)
    hero1 = Hero(castle1)
    hero1.castle.create_monster('Pig', 5)
    hero1.castle.create_monster('Helicopter', 3)
    hero1.castle.create_monster('General', 4)
    
    
    
    
    hero1.check_all_hp()