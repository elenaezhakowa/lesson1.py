from sqlalchemy import create_engine
from sqlalchemy.engine.reflection import Inspector
# from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


def test_db_connection():
    db = create_engine(db_connection_string)
    inspected_tables = Inspector.from_engine(db).get_table_names()

    # Проверяем первую таблицу
    assert inspected_tables[0] == 'company'
    f"Первая таблица должна называться company, а называется {
        inspected_tables[0]}"


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[-1]

    assert row1["id"] == 115
    assert row1["name"] == "Шиномонтаж на "

# def test_db_select():
#     db = create_engine(db_connection_string)
#     with db.connect() as connection:
#         rows = connection.execute("SELECT * FROM company").fetchall()
#         x = 1
#         # Здесь можно добавить логику для обработки результатов
#         for row in rows:
#             print(row)

#     names = db.table_names()
#     assert names[0] == 'company'
