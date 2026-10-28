from zad2.Library import Library


class Book:
    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"A book from {self.library}. {self.number_of_pages} "
                f"pages written by {self.author_name} {self.author_surname} "
                f"published on {self.publication_date}")
