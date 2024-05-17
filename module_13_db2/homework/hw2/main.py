import sqlite3
import csv


def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open(wrong_fees_file, 'r', encoding='windows-1251') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            truck_number = row[0]
            timestamp = row[1]

            sql_request = """
        DELETE FROM table_fees
            WHERE truck_number = ? AND timestamp = ?
        """
            cursor.execute(sql_request, (truck_number, timestamp))


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        delete_wrong_fees(cursor, "../wrong_fees.csv")
        conn.commit()
