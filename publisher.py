class Publisher:
    def __init__(self, name):
        self.name = name

    
    def display(self):
        print(f"Publisher: {self.name}")


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  
        self.title = title
        self.author = author


    def display(self):
        super().display()  
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  
        self.price = price
        self.no_of_pages = no_of_pages

    
    def display(self):
        super().display()  
        print(f"Price: ₹{self.price}")
        print(f"No. of Pages: {self.no_of_pages}")


p1 = Python(
    name="O'Reilly Media",
    title="Learning Python",
    author="Mark Lutz",
    price=850,
    no_of_pages=1648
)


p1.display()
