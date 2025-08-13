trom sqlalchemy import create_engine
from sqlalchemy.sql import text
db_connection_string = "postgresql://x_clients_db_user:5rWd0GLpT4cflfTC4coUxuirTSe0SD2C@dpg-cde2
def test_db_connection():
db = create_engine(db_connection_string)
names = db.table_names()
assert names[0] == 'company'
def test_select():
db = create_engine(db_connection_string)
rows = db.execute("select * from company").fetchall()
row1 = rows[-1]
assert row1["id"] == 115
assert row1["name"] == "Шиномонтаж на Ленинском"
def test_select_1_row():
db = create_engine(db_connection_string)
sql_statement = text("select * from company where id = : company_id")
rows = db.execute(sql_statement, company_id = 112).fetchall()
assert len(rows) == 1
assert rows[0] ["name"] == "Кондитерская Профи-тролли"
def test_select_1_row_with_two_filters():
db = create_engine(db_connection_string)
sql_statement = text("select * from company where \"isActive\" = : isActive and id
>= :id")
my_params = {
    my_params = {
'id': 113,
'isActive': True
rows = db.execute(sql_statement, my_params).fetchall()