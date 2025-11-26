import random as rd


def randomizer_1(n: int, *numbers: list)-> int:
    rand_numb_list = list(range(n))
    for numb in numbers:
        if numb in rand_numb_list:
            rand_numb_list.remove(numb)
    print(rd.choice(rand_numb_list))
    
    


randomizer_1(4, 0, 3)

