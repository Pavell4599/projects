from player import Player
from castle import Castle
from hero import Hero
from map import Map


Pavel = Player('Pavel Rogozin', 'red')
Map1 = Map('Map1')
Castle1 = Castle(Pavel)
hero = Hero(Castle1, Map1)
hero.check_map()
hero.castle.create_monster('Pig', 15)
hero.check_all_hp()
hero.go_outside()
hero.take_monsters_from_castle(group=15)
hero.check_all_hp()








