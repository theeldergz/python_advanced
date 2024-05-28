from typing import List, Tuple

from flask import Flask, render_template, request

from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

from models import init_db, get_all_books, add_new_book, DATA,\
    Book, get_all_books_for_author, get_count_books,\
    get_book_info, get_view_for_book, add_view_to_book

app: Flask = Flask(__name__)


class UpdateBooksForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    author = StringField(validators=[InputRequired()])


class GetAuthorBooks(FlaskForm):
    author = StringField(validators=[InputRequired()])


def _get_html_table_for_books(books: List[dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows: str = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb><td>{count}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],count=book['view_count']
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template(
        'index.html',
        books=get_all_books(),
        number=get_count_books()
    )


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form() -> str:
    UpdateBooksForm()
    if request.method == 'POST':
        new_book = Book(id=None, title=request.form['book_title'], author=request.form['author_name'], view_count=0)
        add_new_book(new_book)
    return render_template('add_book.html')


@app.route('/books/search', methods=['GET', 'POST'])
def search_book() -> str:
    form = GetAuthorBooks()
    if request.method == 'POST':
        author = form.author.data
        return render_template('search_result.html', books=get_all_books_for_author(author=author))
    return render_template('books_for_author.html', form=form)


@app.route('/books/<int:book_id>', methods=['GET'])
def about_book(book_id: int):
    add_view_to_book(book_id)
    return render_template('about_book.html', books=get_book_info(book_id=book_id), book_id=book_id)


if __name__ == '__main__':
    init_db(DATA)
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)

