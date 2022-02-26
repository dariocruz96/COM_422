class Table:
    def __init__(self, number, booking, seats, location):
        self.number = number
        self.booking = booking
        self.seats = seats
        self.location = location

        # Returns readable content

    def __str__(self):
        return f"{self.number} {self.booking} {self.seats} {self.location}"


class Restaurant:
    def __init__(self):
        self.tables_list = []

    def add_table(self, table):
        self.tables_list.append(table)

    def remove_table(self, table_number):
        for i in self.tables_list:
            if i.number == table_number:
                self.tables_list.remove(i)
                return True
        return False

    def new_booking(self, newBooking):
        for i in self.tables_list:
            if newBooking.guests + 2 >= i.seats >= newBooking.guests and i.booking is None and i.location == newBooking.location:
                return i


class Booking:
    def __init__(self, name, guests, location):
        self.name = name
        self.guests = guests
        self.location = location

    def __str__(self):
        return f"{self.name} {self.guests} {self.location}"
