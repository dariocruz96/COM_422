from car import Car


def test_create_car():
    car_one = Car(120, 150, 0)
    assert car_one.currentSpeed == 120
    assert car_one.maxSpeed == 150
    assert car_one.fuelLevel == 0


def test_accelerate():
    car_one = Car(120, 150, 80)
    car_one.accelerate(50)
    assert car_one.fuelLevel == 30


def test_brake():
    car_one = Car(120, 150, 80)
    car_one.brake(50)
    assert car_one.currentSpeed == 70


def test_refuel():
    car_one = Car(120, 150, 80)
    car_one.refuel(50)
    assert car_one.fuelLevel == 100
