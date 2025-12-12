from npc import NPC
from map import Map
import time


class Hero:

    def __init__(self, castle, map):
        self.hero_color = castle.castle_color
        self.hp = 1500
        self.castle = castle
        self.map = map
        self.mons_with_hero_limit = 15


    def check_map(self):
        print()
        print('------Существа на карте-----')
        print()
        all_creature_list = self.map.npcs_list
        for creature_list in all_creature_list:
            for creature in all_creature_list[creature_list]:
                print(creature.name)
        print()
        print('----------------------------')
         
        
    def go_outside(self):
        self.castle.hero_position = 'outside'


    def go_inside(self):
        self.castle.hero_position = 'inside'


    def check_hero_hp(self):
        print()
        print('Здоровье героя:', self.hp)


    def check_monster_hp(self, mon_name: str)-> str:
        print()
        #декоративная шапка со срезом
        defoult_head = '----------------------------'
        right_head = int((28 - len(mon_name)) / 2)
        left_head = 28 - len(mon_name) - right_head
        head = defoult_head[0: left_head] + mon_name + defoult_head[0: right_head]
        print(head)
        #декоративная шапка со срезом

        mon_list = self.castle.mons_in_castle_list[mon_name]
        mon_in_castle_count = len(mon_list)
        is_castle_empty = mon_in_castle_count

        print('В замке:')
        if mon_in_castle_count != 0:
            for i in range(mon_in_castle_count):
                print(f'  {mon_list[i].name}: {mon_list[i].hp} hp')
        if is_castle_empty == 0:
            print(f'  В замке нет {mon_name}')
            
        mon_list = self.castle.mons_with_hero_list[mon_name]
        mon_with_hero_count = len(mon_list)
        is_castle_empty = mon_with_hero_count
        print()
        print('С героем:')
        if mon_with_hero_count != 0:
            for i in range(mon_with_hero_count):
                print(f'  {mon_list[i].name}: {mon_list[i].hp} hp')
        if is_castle_empty == 0:
            print(f'  С героем нет {mon_name}')

        print('----------------------------')
        
        
    def check_all_hp(self)-> str:
        print()
        print('-------Ваше здоровье-------')
        print('Здоровье героя:', self.hp)
        mon_names_list = list(self.castle.mons_with_hero_list.keys())
        
        print()
        print('Монстры в замке:')
        is_castle_empty = 0
        for i in range(len(mon_names_list)):
            mon_name = mon_names_list[i]
            mon_list = self.castle.mons_in_castle_list[mon_name]
            mon_in_castle_count = len(mon_list)
            is_castle_empty += len(mon_list)
            
            if mon_in_castle_count != 0:
                
                for j in range(mon_in_castle_count):
                    print(f'  {mon_list[j].name}: {mon_list[j].hp} hp')
        if is_castle_empty == 0:

            print('  В замке нет монстров') 

        print() 
        print('Монстры с героем:')
        is_hero_empty = 0
        for i in range(len(mon_names_list)):
            mon_name = mon_names_list[i]
            mon_list = self.castle.mons_with_hero_list[mon_name]
            mon_with_hero_count = len(mon_list)
            is_hero_empty += len(mon_list)
            
            if mon_with_hero_count != 0:
                
                for j in range(mon_with_hero_count):
                    print(f'  {mon_list[j].name}: {mon_list[j].hp} hp')
                    
        if is_hero_empty == 0:
            
            print('  Герой без монстров')
                
        
        print('----------------------------')
    
    
    def take_monsters_from_castle(self, group = '', **mon_list)-> list:
        '''
        виды параметра group:
          all -> берете всех монстров из замка к себе, если их меньше лимита
          all_random_(count) -> берете (count) рандомных монстров из замка
          all_(count) -> берете (count) первых монстров из замка
        '''
        if group == '':

            if len(self.castle.mons_with_hero_list) <= self.mons_with_hero_limit:
                is_limit = len(self.castle.mons_with_hero_list)
                for mon_name in mon_list:
                    is_limit += len(mon_list[mon_name])
                if is_limit <= self.mons_with_hero_limit:
                    for mon_name in mon_list:
                        remove_mons_list = []
                        mon_index_list = []

                        for mon in self.castle.mons_in_castle_list[mon_name]:

                            numb_start = mon.name.index(' ') + 1
                            mon_name_index = int(mon.name[numb_start:])
                            mon_index_list.append(mon_name_index)


                        for mon_index in mon_list[mon_name]:
                            try:
                                append_mon_index = mon_index_list.index(mon_index)
                            except ValueError:
                                print()
                                print(f'{mon_name} {mon_index} нету в замке')
                                continue
                            now_append_mon = self.castle.mons_in_castle_list[mon_name][append_mon_index]
                            remove_mons_list.append(now_append_mon)
                            self.castle.mons_with_hero_list[mon_name].append(now_append_mon)
                        
                        for mon in remove_mons_list: 
                            self.castle.mons_in_castle_list[mon_name].remove(mon)
                else:
                    print()
                    print('Вы выбрали слишком много монстров!')
                    print(f'Лимит монстров: {mons_with_hero_limit}.')
            else:
                    print()
                    print('С вами уже максимум монстров!')
                    print(f'Лимит монстров: {mons_with_hero_limit}.')

        elif group == 'all':
            pass


                    
                    
        def send_monsters_to_castle(self, group = '',  **mon_list)-> list:
            '''
            виды параметра group:
            all -> отправляете всех монстров в замок
            '''
            if group == '':
                for mon_name in mon_list:
                        remove_mons_list = []
                        mon_index_list = []

                        for mon in self.castle.mons_with_hero_list[mon_name]:

                            numb_start = mon.name.index(' ') + 1
                            mon_name_index = int(mon.name[numb_start:])
                            mon_index_list.append(mon_name_index)


                        for mon_index in mon_list[mon_name]:
                            try:
                                append_mon_index = mon_index_list.index(mon_index)
                            except ValueError:
                                print()
                                print(f'{mon_name} {mon_index} нету у героя')
                                continue
                            now_append_mon = self.castle.mons_with_hero_list[mon_name][append_mon_index]
                            remove_mons_list.append(now_append_mon)
                            self.castle.mons_in_castle_list[mon_name].append(now_append_mon)
                        
                        for mon in remove_mons_list: 
                            self.castle.mons_with_hero_list[mon_name].remove(mon)
            elif group == 'all':
                for mon_name in self.mon_list:
                        remove_mons_list = []
                        mon_index_list = []

                        for mon in self.castle.mons_with_hero_list[mon_name]:

                            numb_start = mon.name.index(' ') + 1
                            mon_name_index = int(mon.name[numb_start:])
                            mon_index_list.append(mon_name_index)


                        for mon_index in mon_list[mon_name]:
                            
                            now_append_mon = self.castle.mons_with_hero_list[mon_name][mon_index]
                            remove_mons_list.append(now_append_mon)
                            self.castle.mons_in_castle_list[mon_name].append(now_append_mon)
                        
                        for mon in remove_mons_list: 
                            self.castle.mons_with_hero_list[mon_name].remove(mon)
            else:
                print()
                print('Параметр group введен некорректно')
                print('Подсказка:')
                print('  group=all -> отправляете всех монстров в замок')

             
                
    def atack(self, enemy_name: str):
        print()
        result = ''



        enemy_name_in_npcs_list = enemy_name.split('_')[0]
        enemy_list = self.map.npcs_list[enemy_name_in_npcs_list]
        for creature in enemy_list:
            if creature.name == enemy_name:
                enemy = creature
                

        enemy_mon_list = []
        for mon_list in enemy.npc_mon_list:
            for mon in enemy.npc_mon_list[mon_list]:
                enemy_mon_list.append(mon)

        hero_mon_list = []
        for mon_list in self.castle.mons_with_hero_list:
            for mon in self.castle.mons_with_hero_list[mon_list]:
                hero_mon_list.append(mon)


        while True:
             
            
            if len(hero_mon_list) == 0 and len(enemy_mon_list) == 0:
                time.sleep(1)
                result = 'НИЧЬЯ'
                break
            elif len(enemy_mon_list) == 0:
                hero_mon = hero_mon_list[0]
                time.sleep(1)
                print('---ВСЕ МОНСТРЫ ВРАГА УМЕРЛИ!---')
                while enemy.hp > 0:
                    time.sleep(0.45)
                    print(f'{hero_mon.name}: {hero_mon.hp} --> {enemy.name}: {enemy.hp}')
                    enemy.hp -= hero_mon.dmc
                result = 'ВЫ ВЫИГРАЛИ'
                break
            elif len(hero_mon_list) == 0:
                enemy_mon = enemy_mon_list[0]
                time.sleep(1)
                print('---ВСЕ ВАШИ МОНСТРЫ УМЕРЛИ!----')
                while self.hp > 0:
                    time.sleep(0.45)
                    print(f'ВАШ ГЕРОЙ: {self.hp} <-- {enemy_mon.name}: {enemy_mon.hp}')
                    self.hp -= enemy_mon.dmc
                result = 'ВЫ ПРОИГРАЛИ'
                break
                


            enemy_mon = enemy_mon_list[0]
            hero_mon = hero_mon_list[0]
            while (enemy_mon.hp > 0 and hero_mon.hp > 0):
                time.sleep(0.35)
                print(f'{hero_mon.name}: {hero_mon.hp} VS {enemy_mon.name}: {enemy_mon.hp}')
                hero_mon.hp -= enemy_mon.dmc
                enemy_mon.hp -= hero_mon.dmc


            if hero_mon.hp <= 0 and enemy_mon.hp <= 0:
                enemy_mon_list.remove(enemy_mon)
                hero_mon_list.remove(hero_mon)
            elif enemy_mon.hp <= 0:
                enemy_mon_list.remove(enemy_mon)
            elif hero_mon.hp <= 0:
                hero_mon_list.remove(hero_mon)

        
        for mon in enemy_mon_list:
            mon_name = mon.name.split('_')[0]
            enemy.npc_mon_list[mon_name].append(mon)

        for mon in hero_mon_list:
            mon_name = mon.name.split('_')[0]
            self.castle.mons_with_hero_list[mon_name].append(mon)


        time.sleep(3)
        print(f'|-------------> {result} <-------------|')


        

        


if __name__ == '__main__':
    pass


