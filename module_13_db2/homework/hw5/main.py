import sqlite3
from data_for_gen_commands import gen_group


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    sql_insert_in_uefa_com = """
    INSERT INTO uefa_commands (command_name, command_country, command_level)
        VALUES (?, ?, ?)
    """

    sql_insert_in_uefa_draw = """
    INSERT INTO uefa_draw (command_number, group_number)
        VALUES (?, ?)
    """

    sql_get_com_number = """
    SELECT command_number FROM uefa_commands
        WHERE command_name = ?
    """

    for group_num in range(1, number_of_groups + 1):
        group = gen_group()
        cursor.executemany(sql_insert_in_uefa_com, group)

        for command in group:
            command_name = command[0]

            cursor.execute(sql_get_com_number, (command_name,))
            command_number = cursor.fetchone()[0]

            cursor.execute(sql_insert_in_uefa_draw, (command_number, group_num))


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 16): '))
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        generate_test_data(cursor, number_of_groups)
        conn.commit()
