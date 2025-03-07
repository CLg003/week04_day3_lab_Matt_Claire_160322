from flask import render_template, Blueprint, request, redirect
from repositories import author_repository
from repositories import book_repository

from models.author import Author
from models.book import Book

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('/books/index.html', books=books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")  

@books_blueprint.route('/books/<id>', methods=['GET'])   
def show_book(id):
    book = book_repository.select(id)
    return render_template("/books/show.html", book=book)

@books_blueprint.route("/books/new")
def new_book():
    all_authors = author_repository.select_all()
    return render_template("/books/new.html", authors=all_authors)

@books_blueprint.route('/books/new', methods=['POST'])
def save_book():
    if request.form['author'] != "":
        author = author_repository.select(request.form['author'])
    elif request.form['new_author'] != "":
        author = author_repository.save(Author(request.form['new_author']))
    book = Book(request.form['title'], author)
    book_repository.save(book)
    return redirect("/books")
