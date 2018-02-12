class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_percentage):
        tax = self.price * tax_percentage
        self.price += tax
        return self.price

    def return_item(self, reason):
        if (reason == "defective"):
            self.status = "defective"
            self.price = 0
        elif (reason == "unopened"):
            self.status = "for sale"
        else:
            self.status = "used"
            self.price *= 0.8
        return self

    def display_info(self):
        print "Price: " + str(self.price)
        print "Name: " + str(self.name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)

product1 = Product(500, "hard drive", 3, "Yamaha")

product1.display_info()
product1.add_tax(0.18)
product1.return_item("used").sell()
product1.display_info()