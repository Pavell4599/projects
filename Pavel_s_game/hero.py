


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
        print('Здоровье героя: ', self.hp)


    def check_monster_hp(self, monster_name: str)-> str:
        monster_list = self.castle.monsters_in_castle_list[monster_name]
        monster_in_castle_count = len(monster_list)

        print('В замке:')
        if monster_in_castle_count == 0:
            print(f'    Ни одного {monster_name}')
        else:
            for i in range(monster_in_castle_count):
                print(f'    {monster_name}: {monster_list[i].hp} hp')


        monster_list = self.monsters_with_hero_list[monster_name]
        monster_with_hero_count = len(monster_list)

        print('С героем:')
        if monster_with_hero_count == 0:
            print(f'    Ни одного {monster_name}')
        else:
            for i in range(monster_with_hero_count):
                print(f'    {monster_name}: {monster_list[i].hp} hp')
        print()





if __name__ == '__main__':
    player1 = Player('red', 'Pavel_Legendaren')
    castle1 = Castle(player1)
    hero1 = Hero(castle1)
    hero1.castle.create_monster('Pig', 3)
    hero1.check_monster_hp('Pig')
    hero1.castle.create_monster('Helicopter', 2)
    hero1.check_monster_hp('Helicopter')

