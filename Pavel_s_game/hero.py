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
        print()
        print('------Существа на карте-----')
        all_creature_list = self.map.npcs_list
        for creature_list in all_creature_list:
            for creature in all_creature_list[creature_list]:
                print(creature.name)
            
        print('----------------------------')
         
        
    def go_outside(self):
        self.castle.hero_position = 'outside'


    def go_inside(self):
        self.castle.hero_position = 'inside'


    def check_hero_hp(self):
        print()
        print('Здоровье героя:', self.hp)


    def check_monster_hp(self, monster_name: str)-> str:
        print()
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
        print()
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
    
    
    def take_monsters_from_castle(self, **monster_list)-> list:
        
        for monster_name in monster_list:
            remove_monsters_list = []
            for monster_index in monster_list[monster_name]: 
                now_append_monster = self.castle.monsters_in_castle_list[monster_name][monster_index]
                remove_monsters_list.append(now_append_monster)
                self.castle.monsters_with_hero_list[monster_name].append(now_append_monster)
                
            for monster in remove_monsters_list: 
                self.castle.monsters_in_castle_list[monster_name].remove(monster)
                
                
    def send_monsters_to_castle(self, **monster_list)-> list:
        '''
        **monster принимает ...
        '''
        for monster_name in monster_list:
            remove_monsters_list = []
            for monster_index in monster_list[monster_name]: 
                now_append_monster = self.castle.monsters_with_hero_list[monster_name][monster_index]
                remove_monsters_list.append(now_append_monster)
                self.castle.monsters_in_castle_list[monster_name].append(now_append_monster)
                
            for monster in remove_monsters_list: 
                self.castle.monsters_with_hero_list[monster_name].remove(monster)

             
                
    def atack(self, enemy_name: str):
        print()
        result = ''



        enemy_name_in_npcs_list = enemy_name.split('_')[0]
        enemy_list = self.map.npcs_list[enemy_name_in_npcs_list]
        for creature in enemy_list:
            if creature.name == enemy_name:
                enemy = creature
                

        enemy_monster_list = []
        for monster_list in enemy.npc_monster_list:
            for monster in enemy.npc_monster_list[monster_list]:
                enemy_monster_list.append(monster)

        hero_monster_list = []
        for monster_list in self.castle.monsters_with_hero_list:
            for monster in self.castle.monsters_with_hero_list[monster_list]:
                hero_monster_list.append(monster)


        while True:
             
            
            if len(hero_monster_list) == 0 and len(enemy_monster_list) == 0:
                time.sleep(1)
                result = 'НИЧЬЯ'
                break
            elif len(enemy_monster_list) == 0:
                hero_monster = hero_monster_list[0]
                time.sleep(1)
                print('---ВСЕ МОНСТРЫ ВРАГА УМЕРЛИ!---')
                while enemy.hp > 0:
                    time.sleep(0.45)
                    print(f'{hero_monster.name}: {hero_monster.hp} --> {enemy.name}: {enemy.hp}')
                    enemy.hp -= hero_monster.dmc
                result = 'ВЫ ВЫИГРАЛИ'
                break
            elif len(hero_monster_list) == 0:
                enemy_monster = enemy_monster_list[0]
                time.sleep(1)
                print('---ВСЕ ВАШИ МОНСТРЫ УМЕРЛИ!----')
                while self.hp > 0:
                    time.sleep(0.45)
                    print(f'ВАШ ГЕРОЙ: {self.hp} <-- {enemy_monster.name}: {enemy_monster.hp}')
                    self.hp -= enemy_monster.dmc
                result = 'ВЫ ПРОИГРАЛИ'
                break
                


            enemy_monster = enemy_monster_list[0]
            hero_monster = hero_monster_list[0]
            while (enemy_monster.hp > 0 and hero_monster.hp > 0):
                time.sleep(0.35)
                print(f'{hero_monster.name}: {hero_monster.hp} VS {enemy_monster.name}: {enemy_monster.hp}')
                hero_monster.hp -= enemy_monster.dmc
                enemy_monster.hp -= hero_monster.dmc


            if hero_monster.hp <= 0 and enemy_monster.hp <= 0:
                enemy_monster_list.remove(enemy_monster)
                hero_monster_list.remove(hero_monster)
            elif enemy_monster.hp <= 0:
                enemy_monster_list.remove(enemy_monster)
            elif hero_monster.hp <= 0:
                hero_monster_list.remove(hero_monster)

        
        for monster in enemy_monster_list:
            monster_name = monster.name.split('_')[0]
            enemy.npc_monster_list[monster_name].append(monster)

        for monster in hero_monster_list:
            monster_name = monster.name.split('_')[0]
            self.castle.monsters_with_hero_list[monster_name].append(monster)


        time.sleep(3)
        print(f'|-------------> {result} <-------------|')


        

        


if __name__ == '__main__':
    pass


