from player import Player
from castle import Castle
from hero import Hero





player1 = Player('red', 'Pavel_Legendaren')
castle1 = Castle(player1)
hero1 = Hero(castle1)


hero1.castle.create_monster('General', 3)
hero1.castle.create_monster('Helicopter', 3)
hero1.castle.create_monster('General', 3)
hero1.castle.create_monster('Pig', 3)


hero1.check_all_hp()

hero1.take_monsters_from_castle(Pig = [0, 1], General = [1, 3, 4])

hero1.check_all_hp()

hero1.send_monsters_to_castle(Pig = [0], General = [1, 2])

hero1.check_all_hp()


hero1.check_map()

# hero1.check_monster_hp('General')
# hero1.check_monster_hp('Pig')