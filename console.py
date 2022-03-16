import pdb
from models.author import Author
from models.book import Book

import repos.author_repo as author_repo
import repos.book_repo as book_repo

book_repo.delete_all()
author_repo.delete_all()

author_1 = Author("Charles Dickens")
author_repo.save(author_1)
author_2 = Author("Ernest Hemingway")
author_repo.save(author_2)

book_1 = Book("Hard Times", author_1)
book_repo.save(book_1)
book_2 = Book("Great Expectations", author_1)
book_repo.save(book_2)
book_3 = Book("The Old Man and the Sea", author_2)
book_repo.save(book_3)

authors = author_repo.select_all()
for author in authors:
    print(author.__dict__)

books = book_repo.select_all()
for book in books:
    print(book.__dict__)

book_repo.delete(book_1.id)

books = book_repo.select_all()
for book in books:
    print(book.__dict__)


# print(author_repo.select(1).__dict__)


pdb.set_trace()
