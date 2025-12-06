from player import Player
from castle import Castle
from hero import Hero
from map import Map


player = Player('red', 'Gena')
map1 = Map('my map')
dragon_castle = Castle(player)
g = Hero(dragon_castle, map1)



g.check_map()





