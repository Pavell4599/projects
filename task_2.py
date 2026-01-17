import random


def guess(number):
    while not(int(number)):
        number == int(input('Число введено некрооректо, введи его еще раз'))
    print('Число введено корректно')
    
    any_numb = random.randint(-100, 100)
    while True:
        now_ans = input(f'Ваше больше {any_numb}?')
        if now_ans == 'да':
            print(f'Ваше число {any_numb}')
            break
        elif now_ans == 'нет':
            any_numb = int(any_numb / 2)
        else:
            print('Некорретный ответ')
            
            
            

guess(7)
    
        