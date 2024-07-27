class SpaceShip:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def fly(self):
        return f"{self.name} is flying at {self.speed} light years per hour"


class Explorer(SpaceShip):
    def __init__(self, name, speed, sensors):
        super().__init__(name, speed)
        self.sensors = sensors

    def explore(self):
        return f"{self.name} is scanning a planet with {self.sensors} to explore."


class BattleShip(SpaceShip):
    def __init__(self, name, speed, weapons):
        super().__init__(name, speed)
        self.weapons = weapons

    def attack(self):
        return f"{self.name} is attacking with {self.weapons} weapons"
