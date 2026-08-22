# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")
sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from library import Library, Book

library = Library("Central Library")

print(library.name)

print("-" * 30)

book1 = Book("Three Men in a Boat", "J.K.Jerome")
book2 = Book("Norwegian Wood", "Murakami")
book3 = Book("The Courage to Be Disliked", "Ichiro Kishimi")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for book_obj in library.books:
    print(f"{book_obj.title} by {book_obj.author}")

print(f"Added {library.num_books} books.")

print("-" * 30)

library.remove_book(book3)

for book_obj in library.books:
    print(f"{book_obj.title} by {book_obj.author}")

print(f"{library.num_books} books left.")