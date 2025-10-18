class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


t1 = Car("BMW", "X5", 2022)


print(t1)
