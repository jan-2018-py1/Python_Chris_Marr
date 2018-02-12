class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_info(self):
        print "This bike costs " + str(self.price) + " dollars, " + str(self.max_speed) + "mph is the max speed, and " + str(self.miles) + " is the number of miles on this bike."
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self
    
bike1 = Bike(300, 25)
bike2 = Bike(400, 35)
bike3 = Bike(500, 45)

bike1.ride().ride().ride().reverse().display_info()

bike2.ride().ride().reverse().reverse().display_info()

bike3.reverse().reverse().reverse().display_info()