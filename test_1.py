a = {'pis': [2, 3, 2, 2, 5, 9], 'pisa': [2, 3, 2, 2]}
is_10 = 0
for key in a:
    is_10 += len(a[key])


print(is_10)
