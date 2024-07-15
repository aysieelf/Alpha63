class Book:
    id_count = 0

    def __init__(self, title: str, author: str, isbn: str):
        self.id_count = self.id_counter()
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    @classmethod
    def id_counter(cls):
        cls.id_count += 1
        return cls.id_count

    def check_out(self):
        self.is_checked_out = True

    def check_in(self):
        self.is_checked_out = False


class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.checked_out_books = []

    def check_out_book(self, book: Book):
        self.checked_out_books.append(book)
        book.check_out()

    def return_book(self, book: Book):
        self.checked_out_books.remove(book)
        book.check_in()


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def find_book_by_isbn(isbn: str):
        if 







# Test the classes
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")

user1 = User("Alice", "U1")
user2 = User("Bob", "U2")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)

# User1 checks out book1
user1.check_out_book(book1)
print(f"{user1.name} checked out {book1.title}: {book1.is_checked_out}")  # True

# User1 returns book1
user1.return_book(book1)
print(f"{user1.name} returned {book1.title}: {book1.is_checked_out}")  # False

# Finding a book by ISBN
found_book = library.find_book_by_isbn("123456789")
if found_book:
    print(f"Found book: {found_book.title} by {found_book.author}")