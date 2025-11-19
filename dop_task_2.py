import random as rd


def randomizer(n: int, *numbers: dict[int])-> int:
    rand_numb_list = list(range(n))
    for numb in numbers:
        if numb in rand_numb_list:
            rand_numb_list.remove(numb)
    print(rd.choice(rand_numb_list))




randomizer(10, 11, 9, 9, 5, 2, 3, 4, 6, 1, 0)

