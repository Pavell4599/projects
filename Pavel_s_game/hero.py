from npc import NPC
from map import Map
import random as rd
import time
import json


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
        print('Вы вошли в замок')


    def go_inside(self, group = ''):
        '''
        виды параметра group:
          group = 'all' -> когда вы возвращаетесь в замок, 
          то все монстры автоматически уходят из вашего списка
        '''
        self.castle.hero_position = 'inside'
        print()
        print('Вы вышли из замка')
        if group == 'all':
            self.send_monsters_to_castle(group = 'all')


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
          group = 'all' -> берете всех монстров из замка к себе, если их меньше лимита
          group = all_random_(count) -> берете (count) рандомных монстров из замка
          group = (count) -> берете (count) первых монстров из замка
        '''
        mons_with_hero_len = 0
        for mon_name in self.castle.mons_with_hero_list:
            mon_name_list = self.castle.mons_with_hero_list[mon_name]
            mons_with_hero_len += len(mon_name_list)
        mons_in_castle_len = 0 
        for mon_name in self.castle.mons_in_castle_list:
            mon_name_list = self.castle.mons_in_castle_list[mon_name]
            mons_in_castle_len += len(mon_name_list)
        
        if mons_with_hero_len <= self.mons_with_hero_limit:

            if group == '':
                is_limit = mons_with_hero_len
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
                        print(f'Лимит монстров: {self.mons_with_hero_limit}.')
                
            elif str(group).isdigit():
                mon_count = group
                is_limit = mon_count + mons_with_hero_len

                if mon_count <= self.mons_with_hero_limit :
                
                    if is_limit <= mons_in_castle_len:
                        remove_mons_list = []
                        
                        for mon_name in self.castle.mons_in_castle_list:
                            for mon in self.castle.mons_in_castle_list[mon_name]:
                                remove_mons_list.append(mon)
                        
                        for i in range(mon_count):

                            now_append_mon = remove_mons_list[i]
                            name_stop = str(now_append_mon).find(' ')
                            mon_name = str(now_append_mon)[10: name_stop]
                            self.castle.mons_with_hero_list[mon_name].append(now_append_mon)
                            self.castle.mons_in_castle_list[mon_name].remove(now_append_mon)

                    else:
                        print()
                        print(f'Вы не можете выбрать {mon_count} монстров')
                        print(f'В замке меньше {mon_count} монстров')
                else:
                    print()
                    print('Вы выбрали слишком много монстров!')
                    print(f'Лимит монстров: {self.mons_with_hero_limit}.')

            elif group[:7] == 'random_' and str(group[7:]).isdigit():
                mon_count = int(group[7:])
                is_limit = mon_count + mons_with_hero_len

                if mon_count <= self.mons_with_hero_limit :
                
                    if is_limit <= mons_in_castle_len:
                        remove_mons_list = []
                        
                        for mon_name in self.castle.mons_in_castle_list:
                            for mon in self.castle.mons_in_castle_list[mon_name]:
                                remove_mons_list.append(mon)
                        rd.shuffle(remove_mons_list)
                        for i in range(mon_count):

                            now_append_mon = remove_mons_list[i]
                            name_stop = str(now_append_mon).find(' ')
                            mon_name = str(now_append_mon)[10: name_stop]
                            self.castle.mons_with_hero_list[mon_name].append(now_append_mon)
                            self.castle.mons_in_castle_list[mon_name].remove(now_append_mon)

                    else:
                        print()
                        print(f'Вы не можете выбрать {mon_count} монстров')
                        print(f'В замке меньше {mon_count} монстров')
                else:
                    print()
                    print('Вы выбрали слишком много монстров!')
                    print(f'Лимит монстров: {self.mons_with_hero_limit}.')

            else:
                print()
                print('Параметр group введен некорректно')
                print('Подсказка:')
                print('  group = \'all\' -> отправляете всех монстров в замок')
                print('  group = \'random_(count)\' -> берете (count) рандомных монстров из замка')
                print('  group = (count) -> берете (count) монстров из замка по порядку')
        
        else:
            print()
            print('С вами уже максимум монстров!')
            print(f'Лимит монстров: {self.mons_with_hero_limit}.')  

          
    def send_monsters_to_castle(self, group = '',  **mon_list)-> list:
        '''
        виды параметра group:
        group = 'all' отправляете всех монстров в замок
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
            for mon_name in self.castle.mons_with_hero_list:
                    
                    remove_mons_list = []
                    for mon in self.castle.mons_with_hero_list[mon_name]:
                        now_append_mon = mon
                        remove_mons_list.append(now_append_mon)
                        self.castle.mons_in_castle_list[mon_name].append(now_append_mon)
                    
                    for mon in remove_mons_list: 
                        self.castle.mons_with_hero_list[mon_name].remove(mon)
        else:
            
            print('Параметр group введен некорректно')
            print('Подсказка:')
            print('  group = \'all\' -> отправляете всех монстров в замок')

                       
    def atack(self, enemy_name: str, order = ''):
        '''
        order = 'random' -> монстры выходят на сражение в случайном порядке
        '''
        if order == '':

            hero_mon_list = []
            for mon_list in self.castle.mons_with_hero_list:
                for mon in self.castle.mons_with_hero_list[mon_list]:
                    hero_mon_list.append(mon)

        elif order == 'random':
            
            hero_mon_list = []
            for mon_list in self.castle.mons_with_hero_list:
                for mon in self.castle.mons_with_hero_list[mon_list]:
                    hero_mon_list.append(mon)
            rd.shuffle(hero_mon_list)

        else:
            print()
            print('Параметр order введен некорректно')
            print('Подсказка:')
            print('  order = \'random\' -> монстры выходят на сражение в случайном порядке')
            return ''



        print()
        result = ''

        enemy_name_in_npcs_list = enemy_name.split(' ')[0]
        enemy_list = self.map.npcs_list[enemy_name_in_npcs_list]
        for creature in enemy_list:
            if creature.name == enemy_name:
                enemy = creature

        enemy_mon_order = rd.choice(['random', 'by_order'])        
        enemy_mon_list = []
        for mon_list in enemy.npc_mon_list:
            for mon in enemy.npc_mon_list[mon_list]:
                enemy_mon_list.append(mon)
        if enemy_mon_order == 'random':
            rd.shuffle(enemy_mon_list)


        while True:
            
            
            if len(hero_mon_list) == 0 and len(enemy_mon_list) == 0:
                time.sleep(1)
                result = 'НИЧЬЯ'
                break
            elif len(enemy_mon_list) == 0:
                hero_mon = hero_mon_list[0]
                time.sleep(1)
                print()
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
                print()
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
            mon_name = mon.name.split(' ')[0]
            enemy.npc_mon_list[mon_name].append(mon)

        for mon in hero_mon_list:
            mon_name = mon.name.split(' ')[0]
            self.castle.mons_with_hero_list[mon_name].append(mon)


        time.sleep(3)
        print()
        print(f'|-------------> {result} <-------------|')


    def randomize(self, target: str):
        '''
        виды параметра target:
        target='all' -> перемешивание монстров только в замке и у героя
        target='hero'  -> перемешивание монстров только у героя
        target='castle' -> перемешивание монстров только в замке
        '''
        if target == 'all':
            for mon_name in self.castle.mons_in_castle_list:
                        rd.shuffle(self.castle.mons_in_castle_list[mon_name])
            for mon_name in self.castle.mons_with_hero_list:
                        rd.shuffle(self.castle.mons_with_hero_list[mon_name])

        elif target == 'hero':
            for mon_name in self.castle.mons_with_hero_list:
                        rd.shuffle(self.castle.mons_with_hero_list[mon_name])

        elif target == 'castle':
            for mon_name in self.castle.mons_in_castle_list:
                        rd.shuffle(self.castle.mons_in_castle_list[mon_name])
        
        else:
            print()
            print('Параметр target введен некорректно')
            print('Подсказка:')
            print('  target=\'all\' -> перемешивание монстров только в замке и у героя')
            print('  target=\'hero\'  -> перемешивание монстров только у героя')
            print('  target=\'castle\' -> перемешивание монстров только в замке')
            
            
    def save_fig(self):
        hero_mon = self.castle.mons_with_hero_list
        castle_mon = self.castle.mons_in_castle_list
        npcs = self.map.npcs_list
        
        for mon_name in hero_mon:
            for i in range(len(hero_mon[mon_name])):
                mon = hero_mon[mon_name][i]
                new_mon = {}
                new_mon['name'] = mon.name
                new_mon['hp'] = mon.hp
                new_mon['dmc'] = mon.dmc
                hero_mon[mon_name][i] = new_mon
                
        for mon_name in castle_mon:
            for i in range(len(castle_mon[mon_name])):
                mon = castle_mon[mon_name][i]
                new_mon = {}
                new_mon['name'] = mon.name
                new_mon['hp'] = mon.hp
                new_mon['dmc'] = mon.dmc
                castle_mon[mon_name][i] = new_mon
        
        for npc_name in npcs:
            for j in range(len(npcs[npc_name])):
            
                npc = npcs[npc_name][j]
                new_npc = {}
                new_npc['name'] = npc.name
                new_npc['hp'] = npc.hp
                npc_mon = npc.npc_mon_list
                for mon_name in npc_mon:
                    for i in range(len(npc_mon[mon_name])):
                        mon = npc_mon[mon_name][i]
                        new_mon = {}
                        new_mon['name'] = mon.name
                        new_mon['hp'] = mon.hp
                        new_mon['dmc'] = mon.dmc
                        npc_mon[mon_name][i] = new_mon
                
                new_npc['npc_mon_list'] = npc_mon
                npcs[npc_name][j] = new_npc
                
        data = {'castle_mon': castle_mon,'hero_mon': hero_mon, 'npcs': npcs}
        with open('actual_data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        
                
                
                
                
        
        
        
        
        
        
        
        
        



