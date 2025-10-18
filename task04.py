class Movie:

    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def __str__(self):
        return f"Title: {self.title}, Gentre: {self.genre}, Duration: {self.duration}, Rating: {self.rating}"


t1 = Movie("One Piece", "comedy", "440h", 9)


print(t1)
