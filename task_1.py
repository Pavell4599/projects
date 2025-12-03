import matplotlib.pyplot as plt


x = [1, 5, 5, 1, 1]
y = [1, 1, 5, 5, 1]

plt.plot(x, y, color = 'g', 
         label = 'Graf 1', 
         marker = 'o', 
         ms = 5)




#-----Украшения-----
plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.
plt.legend()
plt.title('Base')
plt.grid()
plt.axis('equal')
plt.savefig('task_1.png')

