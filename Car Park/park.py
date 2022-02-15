class Car:
    def __init__(self, registration):
        self.registration = registration

    def __str__(self):
        return f"{self.registration}"


class CarPark:
    def __init__(self):
        self.car_list = []

    def add_car(self, car):
        self.car_list.append(car)

    def remove_car(self, plate):
        self.car_list.remove(plate)

    def __str__(self):
        return self.car_list.__str__()

