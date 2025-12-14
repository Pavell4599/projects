from monsters import General, Skeleton, Pig, Helicopter, Foodman



class Castle:

    def __init__(self, player):
        self.player = player
        self.hp = 1000000
        self.castle_color = self.player.player_color
        self.hero_position = 'inside'
        self.mons_in_castle_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        self.mons_with_hero_list = {'General': [], 'Skeleton': [], 'Pig': [], 'Helicopter': [], 'Foodman': []}
        


    def create_monster(self, mon_name: str, mon_count: int)-> dict:
         
        if self.hero_position == 'inside':
            #Создаем счетчики для всех монстров
            mon_index = len(self.mons_in_castle_list[mon_name]) + len(self.mons_with_hero_list[mon_name])
            #Создаем счетчики для всех монстров
            mon_list = self.mons_in_castle_list[mon_name]
            mon_list_len_before_append = len(self.mons_in_castle_list[mon_name])

            for _ in range(mon_count):
                mon = globals()[mon_name]()
                mon_list.append(mon)
            
            for i in range(mon_list_len_before_append, len(mon_list)):
                mon = mon_list[i]
                mon.name += f' {str(mon_index)}'
                mon_index += 1
            
        
        else:
            print('Вы не можете создавать монстров, находясь на улице')
            
        
    
        
if __name__ == '__main__':
    player_1 = Player('red', 'Pasha_victory_man')
    castle_1 = Castle(player_1)
    castle_1.create_mon('Pig', 2)
    print(castle_1.mons_in_castle_list)
    print(castle_1.mons_in_castle_list['Pig'])