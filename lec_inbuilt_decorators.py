class Planet:
    @staticmethod 
    def is_big_planet(diameter):
        if diameter > 10000:
            return True 
        else:
            return False

print(Planet.is_big_planet(100000))
        