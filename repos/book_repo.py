from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repos.author_repo as author_repo


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    book.id = results[0]['id']
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books

    