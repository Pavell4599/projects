class StarSystem:
    def __init__(self,  planets, name):
        self.planets = list(planets)
        self.name = name

    def __bool__(self):
        return len(self.planets) > 0

sys1 = StarSystem(['p1', 'p2'], 's1')
sys2 = StarSystem([], 's2')

print(bool(sys1))
print(bool(sys2))