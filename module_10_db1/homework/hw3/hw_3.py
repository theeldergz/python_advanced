import sqlite3

counter = 0

with sqlite3.connect("../../../../../Desktop/module_10_db1/homework/hw3/hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT id, COUNT(*) FROM `table_1` ORDER BY `id`")
    result = cursor.fetchall()
    counter += result[0][1]

    print('Задание №1')
    print(f'\tВ 1 таблице {result[0][1]} записей')

    cursor = conn.cursor()
    cursor.execute("SELECT id, COUNT(*) FROM `table_2` ORDER BY `id`")
    result = cursor.fetchall()
    counter += result[0][1]

    print(f'\tВ 2 таблице {result[0][1]} записей')

    cursor = conn.cursor()
    cursor.execute("SELECT id, COUNT(*) FROM `table_3` ORDER BY `id`")
    result = cursor.fetchall()
    counter += result[0][1]

    print(f'\tВ 3 таблице {result[0][1]} записей')
    print(f'\tОбщее кол-во записей {counter}')

    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT value, COUNT(*) FROM `table_1` ORDER BY `value`")
    result = cursor.fetchall()
    counter += result[0][1]

    print('\nЗадание №2')
    print(f'\tВ 1 таблице {result[0][1]} уникальных записей')

    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) from
    (SELECT DISTINCT * FROM `table_1` AS t1
    INTERSECT
    SELECT DISTINCT * FROM `table_2` AS t2)
ORDER BY value""")
    result = cursor.fetchall()

    print('\nЗадание №3')
    print(f'\t{result[0][0]} записи из таблицы table_1 встречается в table_2')

    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) from
    (SELECT DISTINCT * FROM `table_1` AS t1
    INTERSECT
    SELECT DISTINCT * FROM `table_2` AS t2
    INTERSECT
    SELECT DISTINCT * FROM `table_3` AS t3)
ORDER BY value''')
    result = cursor.fetchall()

    print('\nЗадание №4')
    print(f'\tКоличество уникальный записей которые пересекаются во всех таблицах {result[0][0]}')