name = 'Rogozin Pavel'


name_upper = '_'.join(name).upper()
name_ord_upper = []
for symbol in name_upper:
    name_ord_upper.append(ord(symbol))

name_lower = '_'.join(name).lower()
name_ord_lower = []
for symbol in name_lower:
    name_ord_lower.append(ord(symbol))


print(max(name_ord_upper), min(name_ord_upper))
print(max(name_ord_lower), min(name_ord_lower))
