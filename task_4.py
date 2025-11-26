import random as rd


flowers = ['лютик', 'незабудка', 'розы']
colors = ['красный', 'синий', 'голубой', 'оранжевый', 'фиолетовый']
random_colors = [rd.choice(colors) for i in range(len(flowers))]
random_colors = [colors[rd.randint(0, len(colors)-1)] for i in range(len(flowers))]

dict_flowers = dict(zip(flowers, random_colors))


print(dict_flowers)
