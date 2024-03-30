#
# Файл, содеражщий в себе исходный код всех операций с БД
# База данных используется в формате SQLite со встроенное в python библиотекой sqilte3
# База данных хранит в себе информацию в долгострочной перспективе на локальном устройстве
#

import sqlite3 as sql

# переменная для хранения пути до файла БД в формате .db
FILE: str = ""


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
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # сохраняем и закрываем
    db.commit()
    db.close()


# запуск тестирующей части (при неоходимости)
if __name__ == "__main__":
    createDatabase()
