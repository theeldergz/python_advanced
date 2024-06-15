import sqlite3

with sqlite3.Connection(
        r"""C:\Users\Dionis\PycharmProjects\python_advanced\module_16_db3\homework\hw1\test_db.db""") as conn:
    cursor = conn.cursor()
    cursor.executescript("""
     DROP TABLE director;
     DROP TABLE movie;
     DROP TABLE actors;
     DROP TABLE movie_direction;
     """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS director (dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
     dir_first_name VARCHAR, dir_last_name VARCHAR)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS movie (mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
     mov_title VARCHAR(50))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS actors (act_id INTEGER PRIMARY KEY AUTOINCREMENT,
     act_first_name VARCHAR(50), act_last_name VARCHAR(50), act_gender VARCHAR(1))""")

    cursor.execute("""
    CREATE TABLE movie_direction (
    dir_id INTEGER REFERENCES director (dir_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie (mov_id) ON DELETE CASCADE)
    """)

    cursor.execute("""
    CREATE TABLE oscar_awarded (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_id INTEGER REFERENCES movie (mov_id) ON DELETE CASCADE)
    """)

    cursor.execute("""
    CREATE TABLE movie_cast (
    act_id INTEGER REFERENCES actors (act_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie (mov_id) ON DELETE CASCADE,
    role VARCHAR(50))
    """)