def square(stop):
    p = 0
    while True:
        yield p**2
        
        p += 1
        if p == stop:
            break

sq = list(square(10))
print(sq)
