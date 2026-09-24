class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
        self.id = (author, title) 
    def __str__(self): return f"{self.title} by {self.author}"

class EBook(Book): # child
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

class PrintedBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.borrowed = set() 
    @staticmethod
    def validate_year(year): return 1900 <= year <= 2026

    @classmethod
    def from_book_list(cls, name, book_tuples):
        lib = cls(name)
        for t,a,y in book_tuples:
            lib.add_books(Book(t,a,y))
        return lib

    def add_books(self, *books):
        self.books.extend(books)

    def borrow(self, **kwargs): 
        title = kwargs.get('title')
        for b in self.books:
            if b.title == title and b.id not in self.borrowed:
                self.borrowed.add(b.id)
                return f"Borrowed {b}"
        return "Already borrowed"

if __name__ == "__main__":
    lib = Library("National Library")

    lib.add_books(
        PrintedBook("The Idiot", "Fyodor Dostoevsky", 1869, pages=656),
        PrintedBook("1984", "George Orwell", 1949, pages=328)
    )

    print(f"Library: {len(lib.books)} books")
    for book in lib.books:
        print(f" - {book} ({book.year}) ID: {book.id}")

    print("\n" + lib.borrow(title="1984"))
    print(lib.borrow(title="1984"))
    print(f"Borrowed IDs (set): {lib.borrowed}")