import sqlite3


def create_connection(countries):
    conn = None
    try:
        conn = sqlite3.connect(countries)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_table_countries(conn, countries):
    sql = '''INSERT INTO countries (title) VALUES (?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, countries)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_table_cities(conn, countries):
    sql = '''INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, countries)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_table_students(conn, countries):
    sql = '''INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, countries)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_countries_table = '''
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL
    )
'''


sql_cities_table = '''
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL,
    area FLOAT DEFAULT 0,
    country_id INTEGER, 
    FOREIGN KEY(country_id) REFERENCES countries (id)
    )
'''

sql_students_table = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT(200) NOT NULL,
    last_name TEXT(200) NOT NULL,
    city_id INTEGER, 
    FOREIGN KEY(city_id) REFERENCES cities (id)
    )
'''

countries_data = [
    ('Kyrgyzstan',),
    ('Germany',),
    ('China',)
]

connection = create_connection('base_date')
if connection is not None:
    print('Successfully connected to db')
    # create_table(connection, sql_countries_table)
    # create_table(connection, sql_cities_table)
    # create_table(connection, sql_students_table)
    # insert_table_countries(connection, ('Kyrgyzstan',))
    # insert_table_countries(connection, ('Germany',))
    # insert_table_countries(connection, ('China',))
    # insert_table_cities(connection, ('Bishkek', 1288.7, 1))
    # insert_table_cities(connection, ('Berlin', 891.8, 2))
    # insert_table_cities(connection,  ('Beijing', 16410.54, 3))
    # insert_table_cities(connection,   ('Osh', 182.6, 1))
    # insert_table_cities(connection,   ('Munich', 310.43, 2))
    # insert_table_cities(connection,  ('Shanghai', 6340.5, 3))
    # insert_table_cities(connection,   ('Frankfurt', 248.31, 2))
    # insert_table_students(connection,  ('John', 'Doe', 1))
    # insert_table_students(connection,   ('Jane', 'Smith', 2))
    # insert_table_students(connection,   ('Alice', 'Johnson', 3))
    # insert_table_students(connection,   ('Bob', 'Brown', 4))
    # insert_table_students(connection,  ('Charlie', 'Davis', 5))
    # insert_table_students(connection,  ('Emma', 'Wilson', 6))
    # insert_table_students(connection,  ('Ethan', 'Miller', 7))
    # insert_table_students(connection,  ('Olivia', 'Garcia', 1))
    # insert_table_students(connection,  ('Noah', 'Martinez', 2))
    # insert_table_students(connection,   ('Sophia', 'Lopez', 3))
    # insert_table_students(connection,  ('Liam', 'Harris', 4))
    # insert_table_students(connection,  ('Ava', 'Lee', 5))
    # insert_table_students(connection,  ('William', 'Clark', 6))
    # insert_table_students(connection,   ('Mia', 'Young', 7))
    # insert_table_students(connection,  ('James', 'Allen', 1))
    connection.close()


def display_cities():
    conn = sqlite3.connect('base_date')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    print("Список городов из базы данных:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    conn.close()


def display_students_by_city(city_id):
    conn = sqlite3.connect('base_date')
    cursor = conn.cursor()

    query = '''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
               FROM students
               INNER JOIN cities ON students.city_id = cities.id
               INNER JOIN countries ON cities.country_id = countries.id
               WHERE cities.id = ?'''

    cursor.execute(query, (city_id,))
    students = cursor.fetchall()

    if len(students) > 0:
        print(f"Ученики в выбранном городе:")
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, "
                f"Город: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в выбранном городе.")

    conn.close()


# Основная программа
def main():
    display_cities()

    while True:
        try:
            city_id = int(input("\nВведите ID города для отображения учеников (для выхода введите 0): "))

            if city_id == 0:
                print("Программа завершена.")
                break

            display_students_by_city(city_id)
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число.")


if __name__ == "__main__":
    print(
        "Вы можете отобразить список учеников по выбранному ID города из "
        "перечня городов ниже, для выхода из программы введите 0:")
    main()
