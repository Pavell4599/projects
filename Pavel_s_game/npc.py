import random as rd
from monsters import General, Skeleton, Pig, Helicopter, Foodman

class NPC:

    def __init__(self)-> None:
        self.name = rd.choice(['Фермер', 'Боярин', 'Казак', 'Мушкетёр', 'Горожанин'])
        self.hp = rd.randrange(100, 1025, 25)
        self.npc_monster_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        
        for monster_name in self.npc_monster_list:
            for _ in range(rd.randint(1, 3)):
                monster = globals()[monster_name]()
                self.npc_monster_list[monster_name].append(monster)
                

        for monster_name in self.npc_monster_list:
            
            monster_list = self.npc_monster_list[monster_name]
            monster_index = 0
            for i in range(len(monster_list)):
                monster = monster_list[i]
                monster.name += f' {str(monster_index)}'
                monster_index += 1
                


    def npc_list_check(self):
        for monster_name in self.npc_monster_list:
            print(f'{monster_name}:')
            for monster in self.npc_monster_list[monster_name]:
                print('\t', monster.name) 
                      
            



if __name__ == '__main__':
    a = NPC()
    print(a.name)
    print(a.npc_monster_list)
    a.npc_list_check()