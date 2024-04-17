import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""select salaries.id, salaries.salary, count(*) from salaries
                   where salaries.salary <= 5000
                   order by salaries.salary""")
    result = cursor.fetchall()
    print('Задание №1')
    print(f'\t {result[0][1]} людей получает менее 5000 в год ')

    cursor = conn.cursor()
    cursor.execute("select round(avg(salaries.salary), 2) as avg_salary from salaries")
    result = cursor.fetchall()
    print('Задание №2')
    print(f'\tСредняя зарплата жителей составляет {result[0][0]} в год')

    cursor = conn.cursor()
    # cursor.execute("select median(salaries.salary) as avg_salary from salaries")
    cursor.execute("select salary FROM salaries order by salary limit 1 "
                   "offset (select count(salaries.salary) from salaries) / 2")
    result = cursor.fetchall()
    print('Задание №3')
    print(f'\tМедианная зарплата жителей составляет {result[0][0]} в год')

    cursor = conn.cursor()
    cursor.execute("""select sum(salary) from (select * from salaries order by salary
                      desc limit 0.1 * (select count(salary) from salaries))""")

    top_10_percent = cursor.fetchall()[0][0]

    cursor = conn.cursor()
    cursor.execute("""select sum(salary) from (select * from salaries order by salary
                      limit 0.9 * (select count(salary) from salaries))""")

    bot_90_percent = cursor.fetchall()[0][0]
    inequality = 100 * round(top_10_percent / bot_90_percent, 2)

    print('Задание №4')
    print(f'\tПроцент социального неравенства составляет {inequality} %')
