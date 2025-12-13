from npc import NPC
import random as rd


class Map:

    def __init__(self, map_name, fig = '', fig = ''):
        self.map_name = map_name
        self.npcs_list = {'Фермер': [], 'Боярин': [], 'Казак': [], 'Мушкетёр': [], 'Горожанин': []}

        #заполняем список нпс и нумеруем их
        for _ in range(rd.randint(6, 12)):
            npc = NPC()
            self.npcs_list[npc.name].append(npc)

        for npc_name in self.npcs_list:
            now_npc_list = self.npcs_list[npc_name]
            for i in range(len(now_npc_list)):
                now_npc_list[i].name += f' {str(i)}'
        #заполняем список нпс и нумеруем их

 
    def create_npcs(self, npc_count: int)-> list:
        pass
   
