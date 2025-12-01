class Ananist:
    def __init__(self):
        self.name = 'ANANIST'

penis = {'Ananist': [], 'Ananist2': []}
for i in range(5):
    penis['Ananist'].append(Ananist())
    penis['Ananist2'].append(Ananist())



plus_name = 0
for el in penis:
    
    listt = penis[el]
    plus_name = 0
    for i in range(len(listt)):

    # element += str(plus_name)
        listt[i].name += f'_{str(plus_name)}'
        plus_name += 1
   
for i in range(5):

    print(penis['Ananist'][i].name)

