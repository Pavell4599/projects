counter = 0


def update(value):
    global counter
    result = counter + value
    
    print(f'{counter} + {value} = {result}')
    counter = result
    
update(8)
update(4)
update(2)

print(f'{counter = }')