class Car:
    def __init__(self, currentSpeed, maxSpeed, fuelLevel):
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self, value):
        if self.currentSpeed + value < self.maxSpeed:
            self.currentSpeed = self.currentSpeed + value
            self.fuelLevel = self.fuelLevel - value
        elif self.fuelLevel == 0:
            self.currentSpeed = 0
        else:
            self.currentSpeed = self.maxSpeed
            self.fuelLevel = self.fuelLevel - value

    def brake(self, value):
        if self.currentSpeed - value > 0:
            self.currentSpeed = self.currentSpeed - value
        else:
            self.currentSpeed = 0

    def refuel(self, value):
        if 100 >= self.fuelLevel+value >= 0:
            self.fuelLevel = self.fuelLevel + value
        elif self.fuelLevel+value > 100:
            self.fuelLevel = 100
        elif self.fuelLevel+value < 0:
            self.fuelLevel = 0

    def __str__(self):
        return f'{self.currentSpeed} {self.maxSpeed} {self.fuelLevel}'
