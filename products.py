class Product:
    def __init__(self, name, img, price, description): 
        self._name = name
        self.img = img
        self._price = price
        self._description = description

    # Getters 
    def get_name(self):
        return (self._name).strip()
    
    def get_price(self):
        return f"{self._price:.2f}"
    
    def get_description(self):
        return (self._description).strip()
    
    # Setters
    def set_price(self, new_price):
        self._price = new_price

product1 = Product("Chair", "chair.webp", 99, "Stylish chair")
product2 = Product("Counch", "counch.webp", 999, "Stylish counch")

print(product1.get_name())
print(product1.get_price())
print(product1.get_description())

product1.set_price(89.90)
print(product1.get_price())
