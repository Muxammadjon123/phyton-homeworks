class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book titled '{title}' not found.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
            print(f"{member.name} borrowed {book}")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print("Error:", e)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        try:
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"{member.name} returned {book}")
        except BookNotFoundException as e:
            print("Error:", e)

if __name__ == "__main__":
    lib = Library()

    lib.add_book(Book("1984", "George Orwell"))
    lib.add_book(Book("Shatter Me", "Taherah Mafi"))
    lib.add_book(Book("Hobbit", "F. Tolkien"))

    Muxammadjon = Member("Muxammadjon")
    Rustam = Member("Rustam")
    lib.add_member(Muxammadjon)
    lib.add_member(Rustam)

    lib.borrow_book("Muxammadjon", "1984")
    lib.borrow_book("Rustam", "Shatter Me")
    lib.borrow_book("Muxammadjon", "Hobbit")
    lib.borrow_book("Rustam", "Nonexistent book")

    lib.return_book("Muxammadjon", "1984")
    lib.borrow_book("Muxammadjon", "1984")
