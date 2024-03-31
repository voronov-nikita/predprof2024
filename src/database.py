#
# Файл, содеражщий в себе исходный код всех операций с БД
# База данных используется в формате SQLite со встроенное в python библиотекой sqilte3
# База данных хранит в себе информацию в долгострочной перспективе на локальном устройстве
#


import sqlite3 as sql

# переменная для хранения пути до файла БД в формате .db
FILE: str = "data.db"


def createDatabase() -> None:
    '''
    Функция создания новой таблицы в базе данных _._._

    База данных хранит в себе информацию:

    - 1
    - 2
    - 3

    '''

    db = sql.connect(FILE)
    cursor = db.cursor()

    # делаем запрос БД
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS date (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data INTEGER NOT NULL,
            description TEXT NOT NULL
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rooms_count (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data INTEGER NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # data будет разделена _
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS windows_for_room(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # Положения окон формируется по _
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS floors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # сохраняем и закрываем
    db.commit()
    db.close()


def addDataDate(data, description):
    db = sql.connect(FILE)
    cursor = db.cursor()

    cursor.execute(f"""
        INSERT INTO rooms_count(data, description) VALUES('{data}', '{description}')
    """)

    db.commit()
    db.close()

    return "Success"


def addDataRooms(data, description):
    db = sql.connect(FILE)
    cursor = db.cursor()

    cursor.execute(f"""
        INSERT INTO rooms_count(data, description) VALUES('{data}', '{description}')
    """)

    db.commit()
    db.close()

    return "Success"


def addDataWindows(data: list, description: str):
    db = sql.connect(FILE)
    cursor = db.cursor()

    data = '_'.join(data)
    cursor.execute(f"""
        INSERT INTO windows_for_room(data, description) VALUES('{data}', '{description}')
    """)

    db.commit()
    db.close()

    return "Success"


def addDataWindows(data: list, description: str):
    db = sql.connect(FILE)
    cursor = db.cursor()

    data = '_'.join(data)
    cursor.execute(f"""
        INSERT INTO floors(data, description) VALUES('{data}', '{description}')
    """)

    db.commit()
    db.close()

    return "Success"


# запуск тестирующей части (при неоходимости)
if __name__ == "__main__":
    createDatabase()
