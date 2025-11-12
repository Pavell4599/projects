import time 
symbols = 'pythoneeeeerrrrr'


timer = time.time()

symbol_codes = [ord(symbol) for symbol in symbols]

print(time.time() - timer)
print(symbol_codes)

timer = time.time()
out = []
for symbol in range(len(symbols)):
    out.append(symbol)
print(time.time() - timer)



symbols = 'snake'
symbol_codes = (ord(symbol) for symbol in symbols)
# это range, он хранит старт(настоящую позицию), стоп,  степ.
print(symbol_codes)

for object in symbol_codes:
    print(object, end = '-> ')






