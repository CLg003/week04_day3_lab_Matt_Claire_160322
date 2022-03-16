import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Charles Dickens")
author_repository.save(author_1)
author_2 = Author("Ernest Hemingway")
author_repository.save(author_2)

book_1 = Book("Hard Times", author_1)
book_repository.save(book_1)
book_2 = Book("Great Expectations", author_1)
book_repository.save(book_2)
book_3 = Book("The Old Man and the Sea", author_2)
book_repository.save(book_3)

authors = author_repository.select_all()
for author in authors:
    print(author.__dict__)

books = book_repository.select_all()
for book in books:
    print(book.__dict__)

# book_repository.delete(book_1.id)

# books = book_repository.select_all()
# for book in books:
#     print(book.__dict__)


# print(author_repository.select(1).__dict__)


pdb.set_trace()
