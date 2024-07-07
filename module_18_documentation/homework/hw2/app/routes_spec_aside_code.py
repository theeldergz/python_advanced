from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flasgger import APISpec, Swagger
from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from werkzeug.serving import WSGIRequestHandler

from models import (
    DATA,
    get_all_books,
    init_db,
    add_book,
)
from schemas import BookSchema

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



swagger = Swagger(app, template_file='../../../materials/rest_app_example/swagger.json')
api.add_resource(BookList, '/api/books')


if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    init_db(initial_records=DATA)
    app.run('127.0.0.1', debug=True)
