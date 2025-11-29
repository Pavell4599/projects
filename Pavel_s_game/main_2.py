from player import Player
from castle import Castle
from hero import Hero


man = Player('red', 'Gena')
dragon_castle = Castle(man)
gennadiy = Hero(dragon_castle)


gennadiy.castle.create_monster('Pig', 5)
gennadiy.check_all_hp()
gennadiy.take_monsters_from_castle(Pig = [0, 2])
gennadiy.check_all_hp()
gennadiy.send_monsters_to_castle(Pig=[0])
gennadiy.check_all_hp()
gennadiy.check_map()
gennadiy.castle.create_npcs(5)
gennadiy.check_map()
gennadiy.check_monster_hp("Pig")
gennadiy.castle.create_monster('General', 5)
gennadiy.check_monster_hp('General')




