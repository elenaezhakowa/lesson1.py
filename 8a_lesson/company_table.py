from sqlalchemy import create_engine, text


class CompanyTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):
        conn = self.db.connect()
        result = conn.execute(text("SELECT * FROM company WHERE deleted_at IS NULL"))
        rows = result.mappings().all()
        conn.close()
        return rows
