from car import Car

car_one = Car(120, 150, 0)
car_two = Car(80, 120, 0)

print(f'The first car current speed is: {car_one.currentSpeed}, '
      f'max speed is: {car_one.maxSpeed} and '
      f'fuel level is: {car_one.fuelLevel}')
print(f'The second car current speed is: {car_two.currentSpeed}, '
      f'max speed is: {car_two.maxSpeed} and '
      f'fuel level is: {car_two.fuelLevel}')

car_one.brake(5)
car_one.refuel(5)
car_two.accelerate(80)

print(f'The first car current speed is: {car_one.currentSpeed}, '
      f'max speed is: {car_one.maxSpeed} and '
      f'fuel level is: {car_one.fuelLevel}')
print(f'The second car current speed is: {car_two.currentSpeed}, '
      f'max speed is: {car_two.maxSpeed} and '
      f'fuel level is: {car_two.fuelLevel}')
