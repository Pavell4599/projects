fio = 'Rogozin Pavel Dmitrievich'
upper_fio = [ord(symbol) for symbol in fio.upper().replace(' ', '')]
lower_fio = [ord(symbol) for symbol in fio.lower().replace(' ', '')]




print('сумма в upper: ', sum(upper_fio), '\n', 'сумма в lower: ', sum(lower_fio), sep = '')
import time
print(time.localtime())