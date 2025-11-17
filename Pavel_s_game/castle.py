from monsters import *


# from player import *


class Castle:

    def __init__(self, player):
        self.hp = 100000
        self.castle_color = player.player_color
        self.monsters_in_castle_list = {'General': (), 'Skeleton': (), 'Pig': (), 'Helicopter': (), 'Foodman': ()}


    def create_monster(self, monster_name: str, monster_count: int)-> dict:
        self.monsters_in_castle_list[monster_name] = [globals()[monster_name]() for i in range(monster_count)]




# player_1 = Player('red', 'Pasha_victory_man')
# castle_1 = Castle(player_1)
# castle_1.create_monster('Pig', 2)
# print(castle_1.monsters_in_castle_list)
# print(castle_1.monsters_in_castle_list['Pig'])