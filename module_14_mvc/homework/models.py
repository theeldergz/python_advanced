import sqlite3
from typing import Any, Optional, List

DATA: List[dict] = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]


class Book:

    def __init__(self, id: [int, None], title: str, author: str, view_count: int) -> None:
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.view_count: int = view_count

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)


def _create_view_counter_column():
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            ALTER TABLE `table_books`
            ADD view_count INT;
            """
        )


def init_db(initial_records: List[dict]) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='table_books'; 
            """
        )
        exists: Optional[tuple[str,]] = cursor.fetchone()
        # now in `exist` we have tuple with table name if table really exists in DB
        if not exists:
            cursor.executescript(
                """
                CREATE TABLE `table_books` (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    author TEXT)
                """
            )
            cursor.executemany(
                """
                INSERT INTO `table_books`
                (title, author) VALUES (?, ?)
                """,
                [
                    (item['title'], item['author'])
                    for item in initial_records
                ]
            )


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM `table_books`
            """
        )
        return [Book(*row) for row in cursor.fetchall()]


def get_all_books_for_author(author: str) -> List:
    with sqlite3.connect('table_books.db') as conn:
        author = f'%{author}%'
        cursor: sqlite3.Cursor = conn.cursor()
        sql_request = (
            """
            SELECT * FROM `table_books`
                WHERE `author` LIKE ?
            
            """
        )
        cursor.execute(sql_request, (author,))
        return [Book(*row) for row in cursor.fetchall()]


def add_new_book(new_book: Book) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        sql_request = (
            """
            INSERT INTO `table_books`('title', 'author') VALUES (?, ?)
            """
        )

        cursor.execute(sql_request, (new_book['title'], new_book['author']))


def get_count_books() -> int:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        sql_request = (
            """
            SELECT COUNT(id) FROM `table_books`
            """
        )

        cursor.execute(sql_request)
        return cursor.fetchone()[0]


def add_view_to_book(book_id: int):
    with sqlite3.connect('table_books.db') as conn:
        cur_count = get_view_for_book(book_id) + 1
        cursor: sqlite3.Cursor = conn.cursor()
        sql_request = (
            """
            UPDATE `table_books` SET `view_count` = ?
                WHERE `id` = ?
            """
        )

        cursor.execute(sql_request, (cur_count, book_id,))


def get_view_for_book(book_id: int):
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        sql_request = (
            """
            SELECT `view_count` FROM `table_books`
                WHERE `id` = ?
            """
        )

        cursor.execute(sql_request, (book_id,))
        count = cursor.fetchone()

        if count[0] is None:
            count = 0
            return count
        return count[0]


def get_book_info(book_id: int):
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        sql_request = (
            """
            SELECT * FROM `table_books`
                WHERE `id` = ?
            """
        )

        cursor.execute(sql_request, (book_id,))

        return [Book(*row) for row in cursor.fetchall()]
