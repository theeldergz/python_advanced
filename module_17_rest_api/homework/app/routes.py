from typing import Tuple, Any, List

from flask import Flask, request
# from flask_restful import Api, Resource
from flask_restx import Api, Resource
from marshmallow import ValidationError

from models import (
    DATA,
    AUTHORS,
    get_all_books,
    init_db,
    add_book, add_author,
    get_book_by_id, get_all_books_by_authors_id,
    get_author_id,
    delete_book_by_id, delete_author_by_id,
    update_book_by_id,
    Book
)
from schemas import BookSchema, AuthorSchema

app = Flask(__name__)
api = Api(app)


class BookList(Resource):
    def get(self) -> tuple[list[dict], int]:
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> tuple[dict, int]:
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201


class EditBook(Resource):
    def get(self, book_id) -> tuple[Any, int]:
        schema = BookSchema()
        return schema.dump(get_book_by_id(book_id)), 200

    def put(self, book_id):
        data = request.json
        author_name = get_author_id(data['author'])
        print(author_name, data['author'])
        book = Book(title=data['title'], author_id=author_name, id=book_id)

        return update_book_by_id(book), 201

    def delete(self, book_id) -> tuple[Any, int]:
        schema = BookSchema()
        return schema.dump(delete_book_by_id(book_id)), 200


class Author(Resource):
    def post(self):
        data = request.json
        schema = AuthorSchema()

        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        author = add_author(author)
        return schema.dump(author), 201

    def get(self, author_id):
        schema = BookSchema()
        print(get_all_books_by_authors_id(author_id))
        return schema.dump(get_all_books_by_authors_id(author_id), many=True), 200

    def delete(self, author_id):
        schema = AuthorSchema()
        return schema.dump(delete_author_by_id(author_id)), 200


api.add_resource(BookList, '/api/books')
api.add_resource(EditBook, '/api/books/<int:book_id>')
api.add_resource(Author, '/api/authors')
api.add_resource(Author, '/api/authors/<int:author_id>')

if __name__ == '__main__':
    init_db(initial_records=DATA, inital_author_records=AUTHORS)
    app.run(debug=True)
