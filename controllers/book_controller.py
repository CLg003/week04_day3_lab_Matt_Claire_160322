from flask import render_template, Blueprint, request, redirect
from repos import author_repo
from repos import book_repo

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def books():
    books = book_repo.select_all()
    return render_template('/books/index.html', books=books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repo.delete(id)
    return redirect("/books")     
