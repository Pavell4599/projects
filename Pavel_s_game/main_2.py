from player import Player
from castle import Castle
from hero import Hero
from map import Map


player = Player('red', 'Gena')
map1 = Map('my map')
dragon_castle = Castle(player)
g = Hero(dragon_castle, map1)




g.castle.create_monster('Helicopter', 20)
g.check_map()
g.take_monsters_from_castle(Helicopter=[0,1,2,3,4,5,6,7,8,9,10])
g.check_all_hp()
g.atack('Казак_0')






