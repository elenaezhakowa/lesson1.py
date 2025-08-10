from sqlalchemy import create_engine
from sqlalchemy.sql import text
from string import ascii_letters, digits


class StudentTable:
    
    
def __init__(self, connection-string):
        self.db = create_engine(connection-string)


def get_student(self):
    return self.db.execute(self, ("select * from student")).fetchall()


def get_student_by_id(self, id):
    return self.db.execute(self, text("select * from student where id = :select_id"), select_id = id).fetchall()


def get_active_student(self):
    return self.db.execute(self, ("select * from student where \"isActive\" = true")).fetchall()


def delete(self, id):
    return self.db.execute(self, text("delete from student where id = :id_to_delete"))


def create(self, name):
     return self.db.execute(self,  text("insert into company(\"name\") values (:new_name)"), new_name = name)

def get_max_id(self):
    return self.db.execute(self, "select MAX(id) from student").fetchall()[0][0]