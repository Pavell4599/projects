from monsters import General, Skeleton, Pig, Helicopter, Foodman



class Castle:

    def __init__(self, player):
        self.player = player
        self.hp = 1000000
        self.castle_color = self.player.player_color
        self.hero_position = 'inside'
        self.monsters_in_castle_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        self.monsters_with_hero_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        


    def create_monster(self, monster_name: str, monster_count: int)-> dict:
         
        if self.hero_position == 'inside':
            #Создаем счетчики для всех монстров
            monster_index = len(self.monsters_in_castle_list[monster_name]) + len(self.monsters_with_hero_list[monster_name])
            #Создаем счетчики для всех монстров
            monster_list = self.monsters_in_castle_list[monster_name]
            monster_list_len_before_append = len(self.monsters_in_castle_list[monster_name])

            for _ in range(monster_count):
                monster = globals()[monster_name]()
                monster_list.append(monster)
            
            for i in range(monster_list_len_before_append, len(monster_list)):
                monster = monster_list[i]
                monster.name += f'_{str(monster_index)}'
                monster_index += 1
            
        
        else:
            print('Вы не можете создавать монстров, находясь на улице')
            
        
    
        
if __name__ == '__main__':
    player_1 = Player('red', 'Pasha_victory_man')
    castle_1 = Castle(player_1)
    castle_1.create_monster('Pig', 2)
    print(castle_1.monsters_in_castle_list)
    print(castle_1.monsters_in_castle_list['Pig'])