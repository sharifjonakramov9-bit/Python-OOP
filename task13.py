class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False


    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} read")


    def status(self):
        if self.is_read:
            print(f"{self.title} read")
        else:
            print(f"{self.title} not yet read")


book01 = Book("Yolg'iz chiya bo'ri", "Sadullo")
book02 = Book("Xladilnikda 7 ta pamidor bor edi", "Amir")
book03 = Book("Xo'rlangan o'zim", "Sobir")
book04 = Book("Ichimda hayvon bor!", "Sherzod")
book05 = Book("Sevgidan kuygan bolakay", "Sadullo2")
book06 = Book("Qunduz bobo ertaklari", "Qunduz Amaki")


book01.mark_as_read()
book04.mark_as_read()


book01.status()

book02.status()

book03.status()

book04.status()

book05.status()

book06.status()
