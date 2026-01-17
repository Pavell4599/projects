f = open('example_1.txt')

#readline -  команда чтения файла
# print(f.readline(), end = '')
# print(f.readline(), end = '')
# print(f.readline(), end = '')

#next метод
print(next(f), end = '')
print(next(f), end = '\n')

#циклом
f2 = open('example_2.txt')
for i in f2:
    print(i, end = '')

new_f = iter(f)
print(new_f)

f.close()
f2.close()

