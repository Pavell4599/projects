from monsters import General, Skeleton, Pig, Helicopter, Foodman
from npc import NPC
import random as rd



class Castle:

    def __init__(self, player):
        self.hp = 1000000
        self.castle_color = player.player_color
        self.monsters_in_castle_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        self.npcs_list = []
        for _ in range(rd.randint(1, 5)):
            self.npcs_list.append(NPC())


    def create_monster(self, monster_name: str, monster_count: int)-> dict:
        for _ in range(monster_count):
            self.monsters_in_castle_list[monster_name].append(globals()[monster_name]())
            
        
    def create_npcs(self, npc_count: int)-> list:
        for _ in range(npc_count):
            self.npcs_list.append(NPC())
        



if __name__ == '__main__':
    player_1 = Player('red', 'Pasha_victory_man')
    castle_1 = Castle(player_1)
    castle_1.create_monster('Pig', 2)
    print(castle_1.monsters_in_castle_list)
    print(castle_1.monsters_in_castle_list['Pig'])