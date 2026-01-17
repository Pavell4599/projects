def solar_sys_generate():
    for i in ['earth', 'merc', 'saturn', 'solar', 'venus']:
        yield i 
        
planets = solar_sys_generate()
iter_planets = iter(planets)

print(next(iter_planets))
print(next(iter_planets))
print(next(iter_planets))
