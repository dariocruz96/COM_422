import TableBookingSystem


class TestRestaurant:

    def setup_method(self, method):
        self.restaurant = TableBookingSystem.Restaurant()
        self.table1 = TableBookingSystem.Table(1, "Dario", 2, "outside")
        self.table2 = TableBookingSystem.Table(2, "Andre", 5, "outside")
        self.table3 = TableBookingSystem.Table(3, "Luis", 4, "outside")
        self.table4 = TableBookingSystem.Table(4, None, 3, "outside")
        self.table5 = TableBookingSystem.Table(5, None, 2, "outside")
        self.table6 = TableBookingSystem.Table(6, None, 2, "inside")
        self.table7 = TableBookingSystem.Table(7, None, 5, "inside")
        self.table8 = TableBookingSystem.Table(8, None, 4, "inside")
        self.table9 = TableBookingSystem.Table(9, None, 9, "inside")
        self.table10 = TableBookingSystem.Table(10, None, 6, "inside")
        self.restaurant.add_table(self.table1)
        self.restaurant.add_table(self.table2)
        self.restaurant.add_table(self.table3)
        self.restaurant.add_table(self.table4)
        self.restaurant.add_table(self.table5)
        self.restaurant.add_table(self.table6)
        self.restaurant.add_table(self.table7)
        self.restaurant.add_table(self.table8)
        self.restaurant.add_table(self.table9)
        self.restaurant.add_table(self.table10)

    def test_create_table(self):
        assert self.table1.number == 1
        assert self.table1.booking == "Dario"
        assert self.table1.seats == 2
        assert self.table1.location == "outside"

    def test_remove_table(self):
        assert self.restaurant.remove_table(self.table1.number) == True
        assert self.restaurant.remove_table(11) == False

    def test_new_booking(self):
        booking = TableBookingSystem.Booking("Tiago", 4, "inside")
        assert TableBookingSystem.Restaurant.new_booking(self.restaurant, booking) == self.table7
