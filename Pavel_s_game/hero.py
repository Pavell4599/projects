


class Hero:

    def __init__(self, castle):
        self.hero_color = castle.castle_color
        self.hp = 1500
        self.monsters_with_hero_list = {'General': (), 'Skeleton': (), 'Pig': (), 'Helicopter': (), 'Foodman': ()}
        self.position = 'inside'
        self.castle = castle


    def go_outside(self):
        self.position = 'outside'


    def go_inside(self):
        self.position = 'inside'


    def check_hero_hp(self):
        print('Здоровье героя:', self.hp)


    def check_monster_hp(self, monster_name: str)-> str:
        print(f'----------{monster_name}----------')
        
        monster_list = self.castle.monsters_in_castle_list[monster_name]
        monster_in_castle_count = len(monster_list)

        if monster_in_castle_count != 0:
            print('В замке:')
            for i in range(monster_in_castle_count):
                print(f'    {monster_name}: {monster_list[i].hp} hp')
            
        monster_list = self.monsters_with_hero_list[monster_name]
        monster_with_hero_count = len(monster_list)

        if monster_with_hero_count != 0:
            print('С героем:')
            for i in range(monster_with_hero_count):
                print(f'    {monster_name}: {monster_list[i].hp} hp')
        
        print('----------------------------')
        
        
    def check_all_hp(self)-> str:
        print('----------Здоровье----------')
        self.check_hero_hp()
        monster_names_list = list(self.monsters_with_hero_list.keys())
        
        print('В замке:')
        is_castle_empty = 0
        for i in range(len(monster_names_list)):
            monster_name = monster_names_list[i]
            monster_list = self.castle.monsters_in_castle_list[monster_name]
            monster_in_castle_count = len(monster_list)
            is_castle_empty += len(monster_list)
            
            if monster_in_castle_count != 0:
                
                for j in range(monster_in_castle_count):
                    print(f'    {monster_name}: {monster_list[j].hp} hp')
               
                    
        print('В замке:')
        is_hero_empty = 0
        for i in range(len(monster_names_list)):
            monster_name = monster_names_list[i]
            monster_list = self.monsters_with_hero_list[monster_name]
            monster_with_hero_count = len(monster_list)
            is_hero_empty += len(monster_list)
            
            if monster_with_hero_count != 0:
                
                for j in range(monster_with_hero_count):
                    print(f'    {monster_name}: {monster_list[j].hp} hp')
                    
        if is_hero_empty == 0:
            print('    герой без монстров')
                
        
        print('----------------------------')
    
    
    def take_monsters_from_castle(self, **monster_list: dict)-> list:
        # self.castle.monsters_in_castle_list
        pass
        
        














if __name__ == '__main__':
    player1 = Player('red', 'Pavel_Legendaren')
    castle1 = Castle(player1)
    hero1 = Hero(castle1)
    hero1.castle.create_monster('Pig', 3)
    hero1.check_monster_hp('Pig')
    hero1.castle.create_monster('Helicopter', 2)
    hero1.check_monster_hp('Helicopter')

