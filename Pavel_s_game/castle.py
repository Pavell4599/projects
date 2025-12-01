from monsters import General, Skeleton, Pig, Helicopter, Foodman
from npc import NPC
import random as rd



class Castle:

    def __init__(self, player):
        self.player = player
        self.hp = 1000000
        self.castle_color = self.player.player_color
        self.monsters_in_castle_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        self.npcs_list = []
        self.hero = 0 #присвойте этому значению героя
        
        
        for _ in range(rd.randint(1, 6)):
            self.npcs_list.append(NPC())


    def create_monster(self, monster_name: str, monster_count: int)-> dict:

        #Создаем счетчики для всех монстров
        monster_index = len(self.monsters_in_castle_list[monster_name]) + len(self.hero.monsters_with_hero_list[monster_name])
        #Создаем счетчики для всех монстров
         
        if self.hero.position == 'inside':
            monster_list = self.monsters_in_castle_list[monster_name]
            for _ in range(monster_count):
                monster_list.append(globals()[monster_name]())
            
            for i in range(monster_index, len(monster_list)):
                monster = monster_list[i]
                monster.name += f'_{str(i)}'
            
        
        else:
            print('Вы не можете создавать монстров, находясь на улице')
            
        
    
        



if __name__ == '__main__':
    player_1 = Player('red', 'Pasha_victory_man')
    castle_1 = Castle(player_1)
    castle_1.create_monster('Pig', 2)
    print(castle_1.monsters_in_castle_list)
    print(castle_1.monsters_in_castle_list['Pig'])