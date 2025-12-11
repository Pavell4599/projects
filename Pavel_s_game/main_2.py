from player import Player
from castle import Castle
from hero import Hero
from map import Map


player = Player('red', 'Gena')
map_1 = Map('my map')
dragon_castle = Castle(player)
g = Hero(dragon_castle, map_1)




g.castle.create_monster('Helicopter', 10)
g.castle.create_monster('Pig', 10)
# g.check_map()
g.take_monsters_from_castle(Helicopter=[0,1,2,3,4,5])
g.take_monsters_from_castle(Pig=[0,1,2,3,4,5,6,7,8,9])
g.take_monsters_from_castle(Helicopter=[0])
g.check_all_hp()
# g.atack('Фермер_0')






