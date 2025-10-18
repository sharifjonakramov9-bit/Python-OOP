class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = False

    def activate(self):
        self.is_active = True
        print(f"{self.username} onlayn")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} oflayn")
        
    def __str__(self):
        status = "Active" if self.is_active else "Not active"
        return f"Username: {self.username}, Email: {self.email}, Status: {status}"


t1 = User("Ali", "ali@gemail.com")
t1.is_active = True


print(t1)
t1.activate()
print(t1)
t1.deactivate()
print(t1)
