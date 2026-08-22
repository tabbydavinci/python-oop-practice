# Aggregation - one object contains references to one or more INDEPENDENT objects

# has-a relationship

# if I were to delete the Library object then the Book objects would still exist independently

# because the Book objects are created outside the Library and then passed into it

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.num_books = len(self.books)

    def add_book(self, book:Book):
        self.books.append(book)
        self.num_books += 1

    def remove_book(self, book:Book):
        if book in self.books:
            self.books.remove(book)
        self.num_books -= 1

    def list_books(self):
        return self.books

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author