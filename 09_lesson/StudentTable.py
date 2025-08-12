from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:
    def __init__(self, connection_string):
        """Инициализация подключения к базе данных"""
        self.db = create_engine(connection_string)

    def get_students(self):
        """Возвращает всех студентов"""
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT * FROM student"))
            return result.fetchall()

    def get_student_by_user_id(self, user_id):
        """Возвращает запись о конкретном студенте по его user_id"""
        with self.db.connect() as conn:
            result = conn.execute(
                text(
                    "SELECT * FROM student WHERE user_id = :select_user_id"
                    ), {"select_user_id": user_id})
            return result.fetchone()

    def delete_student(self, user_id):
        """Удаляет студента по заданному user_id"""
        with self.db.connect() as conn:
            conn.execute(text(
                "DELETE FROM student WHERE user_id = :user_id_to_delete"
            ), {"user_id_to_delete": user_id})

    def create_student(self, user_id):
        """Создает нового студента"""
        with self.db.connect() as conn:
            conn.execute(text(
                "INSERT INTO student(user_id) VALUES(:new_user_id)"
            ), {"new_user_id": user_id})

    def get_max_user_id(self):
        """Возвращает максимальный user_id среди записей о студентах"""
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT MAX(user_id) FROM student"))
            return result.scalar_one_or_none()

# from sqlalchemy import create_engine
# from sqlalchemy.sql import text
# from string import ascii_letters, digits


# class StudentTable:


# # подключение к БД
# def __init__(self, connection-string):
#         self.db = create_engine(connection-string)

# # получение записи о всех студентах
# def get_student(self):
#     return self.db.execute(self, ("select * from student")).fetchall()

# # получение записи о студенте по ID
# def get_student_by_id(self, id):
#     return self.db.execute(self, text("select * from student where id
# = :select_id"), select_id = id).fetchall()


# # def get_active_student(self):
# #     return self.db.execute(self, ("select * from student where
# \"isActive\" = true")).fetchall()

# # удалить  по id
# def delete(self, id):
#     return self.db.execute(self, text("delete from student
# where id = :id_to_delete"))

# # создать
# def create(self, name):
#      return self.db.execute(self,  text("insert into student(\"name\")
# values (:new_name)"), new_name = name)
# # возвращает по MAX ID
# def get_max_user_id(self):
#     return self.db.execute(self, "select MAX(id) from student"
# ).fetchall()[0][0]

    # def get_active_students(self):
    #     """Возвращает активных студентов"""
    #     with self.db.connect() as conn:
    #         result = conn.execute(
    #             text('SELECT * FROM student WHERE \\"isActive\\" = TRUE'))
    #         return result.fetchall()
