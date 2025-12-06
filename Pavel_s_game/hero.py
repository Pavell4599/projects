from npc import NPC
from map import Map
import time


class Hero:

    def __init__(self, castle, map):
        self.hero_color = castle.castle_color
        self.hp = 1500
        self.castle = castle
        self.map = map


    def check_map(self):
        print('------Существа на карте-----')
        all_creature_list = self.map.npcs_list
        for creature_list in all_creature_list:
            for creature in all_creature_list[creature_list]:
                print(creature.name)
            
        print(self.map.npcs_list)
        print('----------------------------')
        
        
    def go_outside(self):
        self.castle.hero_position = 'outside'


    def go_inside(self):
        self.castle.hero_position = 'inside'


    def check_hero_hp(self):
        print('Здоровье героя:', self.hp)


    def check_monster_hp(self, monster_name: str)-> str:
        #декоративная шапка со срезом
        defoult_head = '----------------------------'
        right_head = int((28 - len(monster_name)) / 2)
        left_head = 28 - len(monster_name) - right_head
        head = defoult_head[0: left_head] + monster_name + defoult_head[0: right_head]
        print(head)
        #декоративная шапка со срезом
        
        monster_list = self.castle.monsters_in_castle_list[monster_name]
        monster_in_castle_count = len(monster_list)

        if monster_in_castle_count != 0:
            print('В замке:')
            for i in range(monster_in_castle_count):
                print(f'    {monster_list[i].name}: {monster_list[i].hp} hp')
            
        monster_list = self.castle.monsters_with_hero_list[monster_name]
        monster_with_hero_count = len(monster_list)

        if monster_with_hero_count != 0:
            print('С героем:')
            for i in range(monster_with_hero_count):
                print(f'    {monster_list[i].name}: {monster_list[i].hp} hp')
        
        print('----------------------------')
        
        
    def check_all_hp(self)-> str:
        print('-------Ваше здоровье-------')
        self.check_hero_hp()
        monster_names_list = list(self.castle.monsters_with_hero_list.keys())
        
        print('Монстры в замке:')
        is_castle_empty = 0
        for i in range(len(monster_names_list)):
            monster_name = monster_names_list[i]
            monster_list = self.castle.monsters_in_castle_list[monster_name]
            monster_in_castle_count = len(monster_list)
            is_castle_empty += len(monster_list)
            
            if monster_in_castle_count != 0:
                
                for j in range(monster_in_castle_count):
                    print(f'    {monster_list[j].name}: {monster_list[j].hp} hp')
               
                    
        print('Монстры с героем:')
        is_hero_empty = 0
        for i in range(len(monster_names_list)):
            monster_name = monster_names_list[i]
            monster_list = self.castle.monsters_with_hero_list[monster_name]
            monster_with_hero_count = len(monster_list)
            is_hero_empty += len(monster_list)
            
            if monster_with_hero_count != 0:
                
                for j in range(monster_with_hero_count):
                    print(f'    {monster_list[j].name}: {monster_list[j].hp} hp')
                    
        if is_hero_empty == 0:
            print('    герой без монстров')
                
        
        print('----------------------------')
    
    
    def take_monsters_from_castle(self, **monster_list: dict)-> list:
        
        for monster_name in monster_list:
            remove_monsters_list = []
            for monster_index in monster_list[monster_name]: 
                now_append_monster = self.castle.monsters_in_castle_list[monster_name][monster_index]
                remove_monsters_list.append(now_append_monster)
                self.castle.monsters_with_hero_list[monster_name].append(now_append_monster)
                
            for monster in remove_monsters_list: 
                self.castle.monsters_in_castle_list[monster_name].remove(monster)
                
                
    def send_monsters_to_castle(self, **monster_list: dict)-> list:
        
        for monster_name in monster_list:
            remove_monsters_list = []
            for monster_index in monster_list[monster_name]: 
                now_append_monster = self.castle.monsters_with_hero_list[monster_name][monster_index]
                remove_monsters_list.append(now_append_monster)
                self.castle.monsters_in_castle_list[monster_name].append(now_append_monster)
                
            for monster in remove_monsters_list: 
                self.castle.monsters_with_hero_list[monster_name].remove(monster)

             
                
    def atack(enemy_name: str, **monster_list: dict):
        fight_counter = 0
        result = ''
        enemy_name_in_npcs_list = enemy_name.split('_')[0]
        enemy_list = self.map.npcs_list[enemy_name_in_npcs_list]
        for creature in enemy_list:
            if creature.name == enemy_name:
                enemy = creature
                
        while True:
            enemy_monster_list = enemy.npc_monster_list
            hero_monster_list = monster 
            if len(enemy_monster_list) == 0:
                pass
            elif len(enemy_monster_list) == 0:
                pass
            else:
                result = '>>>>>>>>>>_НИЧЬЯ_<<<<<<<<<<<'


            enemy_monster = enemy_monster_list[0]
            hero_monster = hero_monster_list[0]
            while (enemy_monster.hp <= 0 or hero_monster.hp <= 0):




            

        


    
            
            
       

if __name__ == '__main__':


