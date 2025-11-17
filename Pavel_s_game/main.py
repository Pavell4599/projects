from player import *
from castle import *
from hero import *





player1 = Player('red', 'Pavel_Legendaren')
castle1 = Castle(player1)
hero1 = Hero(castle1)
hero1.castle.create_monster('Pig', 3)
hero1.check_monster_hp('Pig')

hero1.castle.create_monster('Helicopter', 2)
hero1.check_monster_hp('Helicopter')