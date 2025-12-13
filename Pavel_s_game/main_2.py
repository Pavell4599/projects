from player import Player
from castle import Castle
from hero import Hero
from map import Map


player = Player('red', 'Gena')
map_1 = Map('my map')
dragon_castle = Castle(player)
g = Hero(dragon_castle, map_1)




g.castle.create_monster('Pig', 20)
g.castle.create_monster('Foodman',10)

g.randomize('castle')

# g.check_map()
# g.take_monsters_from_castle(Pig=[0,2,3,4,7,11])
# g.take_monsters_from_castle(group = 15)
g.check_all_hp()
# g.go_inside(group = 'all')
# g.check_all_hp()

# g.send_monsters_to_castle(group = 'all')

# g.check_all_hp()
# g.check_monster_hp('Helicopter')









