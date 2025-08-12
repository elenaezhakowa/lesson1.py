# from sqlalchemy import create_engine

# db_connection_string = "postgresql://
# postgres:19091947gG!@@localhost:5432/tu_db"


# def test_db_connection():
#     db = create_engine(db_connection_string)
#     names = db.table_names()
#     assert names[0] == 'student'

from sqlalchemy import create_engine, inspect


db_connection_string = "postgresql://postgres:19091947gG!@localhost:5432/tu_db"


def test_db_connection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)

    # Получаем список таблиц
    names = inspector.get_table_names()

    # Проверяем наличие таблицы 'student'
    assert 'student' in names
