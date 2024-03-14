from typing import List, Set

class Book:
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author
        self.category = category

class Shelf:
    def __init__(self):
        self.books: List[Book] = []
        self.categories: Set[str] = set()

    def add_book(self, book: Book):
        self.books.append(book)
        self.categories.add(book.category)

    def sort_books(self):
        self.books.sort(key=lambda x: x.title)

def organize_books(books: Set[Book]) -> List[Shelf]:
    shelves = {}
    for book in books:
        if book.category not in shelves:
            shelves[book.category] = Shelf()
        shelves[book.category].add_book(book)
    return list(shelves.values())

def print_shelves(shelves: List[Shelf]):
    for shelf in shelves:
        print(f"Shelf categories: {shelf.categories}")
        for book in shelf.books:
            print(f"Title: {book.title}, Author: {book.author}, Category: {book.category}")

# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Classic")
book3 = Book("1984", "George Orwell", "Dystopian")

books = {book1, book2, book3}

shelves = organize_books(books)
for shelf in shelves:
    shelf.sort_books()

print_shelves(shelves)
