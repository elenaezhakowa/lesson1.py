from sqlalchemy import create_engine

db_connection_string = "postgresql:// postgres:19091947gG!@localhost:5432/moya_baza_2"


def test_db_connection():
    db = create_engine(db_connection_string)
    names == db.table_names()
    assert names[0] == 'student'
