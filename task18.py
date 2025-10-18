class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    
    def info(self):
        print(f"Name: {self.name}, Price: {self.price}")

    def __str__(self):
        return f"{self.name} {self.price}$ {self.category}"


t1 = Product("Ananas", 20, "vegetables")
t2 = Product("Nok", 30, "vegetables")
t3 = Product("Olma", 10, "vegetables")
t4 = Product("Uzum", 15, "vegetables")
t5 = Product("Banan", 5, "vegetables")
t6 = Product("Lemon", 40, "vegetables")


products = [t1, t2, t3, t4, t5, t6]

mx = max(products, key=lambda e: e.price)

print(mx)
