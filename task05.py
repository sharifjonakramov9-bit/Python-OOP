class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.is_active = False
        
    def __str__(self):
        return f"{self.name} {self.price} {self.category} ({self.is_active})"


t1 = Product("Ananas", 20, "electronics")
t1.is_active = True


print(t1)

