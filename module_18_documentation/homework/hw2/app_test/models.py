import sqlite3
from dataclasses import dataclass
from typing import Optional, Union, List, Dict

DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author_id': '1'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author_id': '2'},
    {'id': 3, 'title': 'War and Peace', 'author_id': '3'},
]

AUTHORS = [{'first_name ': 'Swaroop', 'last_name ': 'Chakraborty.', 'middle_name ': 'H'},
           {'first_name ': 'Herman', 'last_name ': 'Melville', 'middle_name ': ''},
           {'first_name ': 'Leo', 'last_name ': 'Tolstoy', 'middle_name ': ''}]

DATABASE_NAME = 'test_hw_17.db'
BOOKS_TABLE_NAME = 'books'


@dataclass
class Book:
    title: str
    author_id: Optional[int] = None
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)


@dataclass
class Author:
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    author_id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[Dict], inital_author_records: List[Dict]) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{BOOKS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                """
                CREATE TABLE `author`(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    middle_name TEXT NULL
                );
                """)

            cursor.executemany(
                f"""
                            INSERT INTO `author`
                            (first_name, last_name, middle_name) VALUES (?, ?, ?)
                            """,
                [
                    (item['first_name '], item['last_name '], item['middle_name '],)
                    for item in inital_author_records
                ]
            )

            cursor.executescript(
                f"""
                CREATE TABLE `{BOOKS_TABLE_NAME}`(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT,
                    author_id INTEGER NOT NULL REFERENCES author(id) ON DELETE CASCADE
                );
                """
            )
            cursor.executemany(
                f"""
                INSERT INTO `{BOOKS_TABLE_NAME}`
                (title, author_id) VALUES (?, ?)
                """,
                [
                    (item['title'], item['author_id'])
                    for item in initial_records
                ]
            )


def _get_book_obj_from_row(row: tuple) -> Book:
    return Book(id=row[0], title=row[1], author_id=row[2])


def _get_author_from_row(row: tuple) -> Author:
    return Author(first_name=row[0], last_name=row[1], middle_name=row[2], author_id=row[3])


def get_all_books() -> list[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM `{BOOKS_TABLE_NAME}`')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def add_book(book: Book) -> Book:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO `{BOOKS_TABLE_NAME}` 
            (title, author) VALUES (?, ?)
            """,
            (book.title, book.author_id)
        )
        book.id = cursor.lastrowid
        return book


def add_author(author: Author) -> Author:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO author 
            (first_name, last_name, middle_name) VALUES (?, ?, ?)
            """,
            (author.first_name, author.last_name, author.middle_name)
        )
        author.id = cursor.lastrowid
        return author


def get_book_by_id(book_id: int) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE id = ?
            """,
            (book_id,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(book: Book) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE {BOOKS_TABLE_NAME}
            SET title = ?, author_id = ?
            WHERE id = ?
            """,
            (book.title, book.author_id, book.id)
        )
        conn.commit()


def delete_book_by_id(book_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            DELETE FROM {BOOKS_TABLE_NAME}
            WHERE id = ?
            """,
            (book_id,)
        )
        conn.commit()


def delete_author_by_id(author_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")
        cursor.execute(
            f"""
            DELETE FROM author
            WHERE id = ?
            """,
            (author_id,)
        )
        conn.commit()


def get_book_by_title(book_title: str) -> Optional[Book]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE title = ?
            """,
            (book_title,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def get_all_books_by_authors_id(author_id: int) -> list:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE author_id = ?
            """,
            (author_id,)
        )
        book_list = [_get_book_obj_from_row(row) for row in cursor.fetchall()]
        if book_list:
            return book_list


def get_author_id(authors_name: str):
    with sqlite3.connect(DATABASE_NAME) as conn:
        authors_name = f'%{authors_name}%'.lower()
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT id FROM `author` 
                WHERE first_name LIKE ?
                OR last_name LIKE ?
                OR middle_name LIKE ?
            """,
            (authors_name, authors_name, authors_name)
        )
        authors_id = cursor.fetchone()

        if authors_id:
            return authors_id[0]


def __drop_tables():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE authors")
        cursor.execute("DROP TABLE books")

# __drop_tables()
