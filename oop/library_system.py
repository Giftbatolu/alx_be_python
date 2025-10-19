"""A library system with Book, EBook, PrintBook, and Library classes."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []
        self.bbook = Book
        self.ebook = EBook
        self.pbook = PrintBook

    def add_book(self, book):
        if isinstance(book, (self.bbook, self.ebook, self.pbook)):
            self.books.append(book)
        else:
            raise Exception
    
    def list_books(self):
        for book in self.books:
            print(f"{book}")