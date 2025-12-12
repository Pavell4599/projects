from player import Player
from castle import Castle
from hero import Hero
from map import Map


player = Player('red', 'Gena')
map_1 = Map('my map')
dragon_castle = Castle(player)
g = Hero(dragon_castle, map_1)




g.castle.create_monster('Helicopter', 10)

# g.check_map()
g.take_monsters_from_castle(Helicopter=[0,1])
g.take_monsters_from_castle(Helicopter=[7,8,11])
g.send_monsters_to_castle(Helicopter=[0,1])

g.check_all_hp()
g.check_monster_hp('Helicopter')
# g.atack('Фермер_0')






