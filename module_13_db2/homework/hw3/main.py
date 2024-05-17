import datetime
import sqlite3


# def create_table(cursor: sqlite3.Cursor, table_name='birds_info'):
#     cursor.execute(f"""CREATE TABLE {table_name}
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#          name_bird TEXT NOT NULL, count_bird INTEGER NOT NULL)""")


def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    sql_request = """INSERT INTO birds_info(name_bird, timestamp) VALUES (?, ?)"""
    cursor.execute(sql_request, (bird_name, date_time))


def check_if_such_bird_already_seen(
        cursor: sqlite3.Cursor,
        bird_name: str
) -> bool:
    sql_request = """
    SELECT * FROM birds_info
        WHERE EXISTS 
                (SELECT * FROM birds_info WHERE name_bird = ?)
    """
    cursor.execute(sql_request, (bird_name,))

    return bool(cursor.fetchone())


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name: str = input("Пожалуйста введите имя птицы\n> ")
    right_now: str = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("../homework.db") as connection:
        cursor: sqlite3.Cursor = connection.cursor()
        log_bird(cursor, name, right_now)

        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
