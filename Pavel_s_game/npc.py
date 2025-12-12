import random as rd
from monsters import General, Skeleton, Pig, Helicopter, Foodman

class NPC:

    def __init__(self)-> None:
        self.name = rd.choice(['Фермер', 'Боярин', 'Казак', 'Мушкетёр', 'Горожанин'])
        self.hp = rd.randrange(400, 1025, 25)
        self.npc_mon_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        
        for mon_name in self.npc_mon_list:
            for _ in range(rd.randint(1, 3)):
                mon = globals()[mon_name]()
                self.npc_mon_list[mon_name].append(mon)
                

        for mon_name in self.npc_mon_list:
            
            mon_list = self.npc_mon_list[mon_name]
            mon_index = 0
            for i in range(len(mon_list)):
                mon = mon_list[i]
                mon.name += f' {str(mon_index)}'
                mon_index += 1
                


    def npc_list_check(self):
        for mon_name in self.npc_mon_list:
            print(f'{mon_name}:')
            for mon in self.npc_mon_list[mon_name]:
                print('\t', mon.name) 
                      
            



if __name__ == '__main__':
    a = NPC()
    print(a.name)
    print(a.npc_mon_list)
    a.npc_list_check()