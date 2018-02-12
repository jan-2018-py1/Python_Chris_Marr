# Create a class called  Car. In the__init__(), allow the user to specify the 
# following attributes: price, speed, fuel, mileage. If the price is greater 
# than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method 
# called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information about
#  the car once the attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (mileage > 10000):
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)

mustang = Car(5000, 160, "full", 22)
ferrari = Car(120000, 240, "empty", 23)
lambo = Car(180000, 220, "full", 24)
bmw = Car(67000, 160, "half", 25)
lexus = Car(55000, 160, "full", 26)
camaro = Car(28000, 160, "full", 27)

mustang.display_all()
ferrari.display_all()
lambo.display_all()
bmw.display_all()
lexus.display_all()
camaro.display_all()