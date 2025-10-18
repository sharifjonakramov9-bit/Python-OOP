class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.is_active = False
        
    def __str__(self):
        s = (
            f"{self.name} omborda mavjud" if self.is_active else f"{self.name} hozirda tugagan"
        )
        return f"{self.name} - {self.price}$ \n{self.category} ({self.is_active})"


t1 = Product("Ananas", 20, "electronics")
t1.is_active = True 


print(t1)

