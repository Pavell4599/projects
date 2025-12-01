from player import Player
from castle import Castle
from hero import Hero


player = Player('red', 'Gena')
dragon_castle = Castle(player)
g = Hero(dragon_castle)
dragon_castle.hero = g


g.castle.create_monster('Pig', 5)
g.take_monsters_from_castle(Pig=[0,2])
g.go_outside()
g.castle.create_monster('Pig', 5)
g.check_all_hp()
g.go_inside()
g.castle.create_monster('Pig', 5)
g.check_all_hp()




