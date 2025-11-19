# Функция ord переводит символы в их ASCII коды
# А функция chr производит обратную операцию

text = "Hello"

for symbol in text:
    print(ord(symbol), end="; ")
print()

codes = [119, 111, 114, 108, 100]
symbols = ""

for code in codes:
    symbols += chr(code)

print(symbols)