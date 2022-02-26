import park

car_park = park.CarPark()
occupied = 0
max_size = 15
vacant = max_size
car_park2 = ["plate"]
print("Welcome to our park")
while True:
    choice = int(input("1 - Car arriving\n"
                       "2 - Car departing\n"
                       "3 - List of cars parked\n"))
    if choice == 1:
        print(f"Currently we got {vacant} vacant and {occupied} occupied spaces.")
        if vacant == 0:
            print("We are sorry but it is not possible for you to park at the moment.")
        elif 0 < vacant <= max_size:
            plate = input("Please input the car plate number:\n")
            if plate in car_park.car_list:
                print("Alert! This car is already registered!")
            else:
                occupied += 1
                vacant -= 1
                new_car = park.Car(plate)
                car_park.add_car(str(new_car))
                print("Car added to parking list.")
                print(f"Currently we got {vacant} vacant and {occupied} occupied spaces.")

    elif choice == 2:
        if occupied > 0:
            plate = int(input("Please input the car plate number:\n"))
            occupied -= 1
            vacant += 1
            car_park.remove_car(str(plate))
            print("Car removed from parking list.")
            print(f"Currently we got {vacant} vacant and {occupied} occupied spaces.")
        else:
            print("There are no cars inside.")
    elif choice == 3:
        if occupied == 0:
            print("There are no cars inside.")
        else:
            print(car_park)
