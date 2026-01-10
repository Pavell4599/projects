class StarSystem:
    def __init__(self,  planets, name):
        self.planets = list(planets)
        self.name = name

    def __getitem__(self, key):
        print(self.planets[key])

sys1 = StarSystem(['p1', 'p2'], 's1')
sys1[0]
sys1[0:2]