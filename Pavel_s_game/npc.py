import random as rd
from monsters import *

class NPC:

    def __init__(self)-> None:
        self.hp = rd.randrange(100, 1025, 25)
        self.npc_monster_list = {'General': (), 'Skeleton': (), 'Pig': (), 'Helicopter': (), 'Foodman': ()}
        for key in self.npc_monster_list:
            monster_class_name = globals()[key]()
            self.npc_monster_list[key] = [monster_class_name for i in range (rd.randint(1, 4))]



if __name__ == '__main__':
    a = NPC()
    print(a.npc_monster_list)