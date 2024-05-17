import sqlite3


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
        name: str,
) -> None:
    handle_name = f"%{name}"
    max_salary = 100000
    sql_request = """
SELECT salary FROM table_effective_manager
    WHERE name LIKE ?
"""
    new_salary = round(int(cursor.execute(sql_request, (handle_name,)).fetchone()[0]) * 1.1)
    if new_salary <= max_salary:
        sql_request_up_salary = """
        UPDATE table_effective_manager SET salary=?
            WHERE name LIKE ?
        """
        cursor.execute(sql_request_up_salary, (new_salary, handle_name))
    else:
        sql_request_del_employee = """
        DELETE FROM table_effective_manager WHERE name LIKE ?
        """
        cursor.execute(sql_request_del_employee, (handle_name,))


if __name__ == '__main__':
    name: str = input('Введите имя сотрудника: ')
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, name)
        conn.commit()
