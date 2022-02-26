from Car import Car


def setup_module(module):
    print("----------Start car-----------")


def teardown_module(module):
    print("-----------End car------------")


class TestCar:

    def setup_method(self, method):
        self.car_one = Car(120, 50, 0)
        self.car_two = Car(120, 150, 80)

    def test_create_car(self):
        assert self.car_one.currentSpeed == 120
        assert self.car_one.maxSpeed == 50
        assert self.car_one.fuelLevel == 0

    def test_accelerate(self):
        self.car_two.accelerate(50)
        assert self.car_two.fuelLevel == 30

    def test_brake(self):
        self.car_two.brake(50)
        assert self.car_two.currentSpeed == 70

    def test_refuel(self):
        self.car_two.refuel(50)
        assert self.car_two.fuelLevel == 100
