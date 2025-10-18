class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = False
        
    def __str__(self):
        return f"{self.username} {self.email} ({self.is_active})"


t1 = User("Ali", "ali@gemail.com")
t1.is_active = True


print(t1)

