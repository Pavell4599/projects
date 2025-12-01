from npc import NPC


class Hero:

    def __init__(self, castle):
        self.hero_color = castle.castle_color
        self.hp = 1500
        self.monsters_with_hero_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        self.position = 'inside'
        self.castle = castle


    def check_map(self):
        print('------Существа на карте-----')
        print(self.castle.npcs_list)
        print('----------------------------')
        
        
    def go_outside(self):
        self.position = 'outside'
        self.castle.hero_position = 'outside'


    def go_inside(self):
        self.position = 'inside'
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
            
        monster_list = self.monsters_with_hero_list[monster_name]
        monster_with_hero_count = len(monster_list)

        if monster_with_hero_count != 0:
            print('С героем:')
            for i in range(monster_with_hero_count):
                print(f'    {monster_list[i].name}: {monster_list[i].hp} hp')
        
        print('----------------------------')
        
        
    def check_all_hp(self)-> str:
        print('-------Ваше здоровье-------')
        self.check_hero_hp()
        monster_names_list = list(self.monsters_with_hero_list.keys())
        
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
            monster_list = self.monsters_with_hero_list[monster_name]
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
                self.monsters_with_hero_list[monster_name].append(now_append_monster)
                
            for monster in remove_monsters_list: 
                self.castle.monsters_in_castle_list[monster_name].remove(monster)
                
                
    def send_monsters_to_castle(self, **monster_list: dict)-> list:
        
        for monster_name in monster_list:
            remove_monsters_list = []
            for monster_index in monster_list[monster_name]: 
                now_append_monster = self.monsters_with_hero_list[monster_name][monster_index]
                remove_monsters_list.append(now_append_monster)
                self.castle.monsters_in_castle_list[monster_name].append(now_append_monster)
                
            for monster in remove_monsters_list: 
                self.monsters_with_hero_list[monster_name].remove(monster)

             
                
    def atack(self):
        pass


    #специальный метод  
    def create_npcs(self, npc_count: int)-> list:
        for _ in range(npc_count):
            self.castle.npcs_list.append(NPC())
    #специальный метод 
            
            
       
if __name__ == '__main__':
    from player import Player
    player1 = Player('red', 'Pavel_Legendaren')
    castle1 = Castle(player1)
    hero1 = Hero(castle1)
    hero1.castle.create_monster('Pig', 3)
    hero1.check_monster_hp('Pig')
    hero1.castle.create_monster('Helicopter', 2)
    hero1.check_monster_hp('Helicopter')

