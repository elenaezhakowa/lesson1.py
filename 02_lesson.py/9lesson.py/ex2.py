from book import Book

library = [
    Book("Мир", "Толстой"),
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee")
]

for book in library:
    print(f"{book.title} - {book.author}")
