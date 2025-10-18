class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} read")

    def status(self):
        self.is_read = False
        print(f"{self.title} not yet read")
        
    def __str__(self):
        s = "Read" if self.is_read else "Not Read"
        return f"Title: {self.title}, Author: {self.author}, Status: {s}"


t1 = Book("Ali", "ali@gemail.com")
t1.is_read = True


print(t1)
t1.mark_as_read()
print(t1)
t1.status()
print(t1)
