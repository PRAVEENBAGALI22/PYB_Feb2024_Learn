class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} - {self.available}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book, {book}")

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self,book_title,member):
        for book in self.books:
            if book.title == book_title and book.available:
                book.available = False
                member.borrowed_book.append(book)
                print(f"Book {book_title} borrowed by {member.name}")
                return
            print(f"Book, {book_title} is not available")



class Member:
    pass


b1 = Book("PYB", "QA")
b2 = Book("PB", "FRD")
b3 = Book("PK", "NITK")
print(b1)
print(b2)
print(b3)

l1 = Library()
l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)

l1.display_books()