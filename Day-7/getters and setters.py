class car:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_value):
        self._price = new_value // 10  # Update the _price attribute directly
    
    def show(self):
        print(f"The price of that car is: {self._price}")

    
# Create an object of the car class with an initial price
obj = car(78009800)
# Display the initial price
obj.show()
# Update the price using the setter
obj.price = 456789000
# Display the updated price
obj.show()
