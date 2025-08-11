from StudentApi import StudentApi
from StudentTable import StudentTable

# Подключение к API и БД
# Здесь укажи настоящий URL или endpoint своего API
# ? api = CompanyApi("http://5.101.50.27:8000")
api = StudentApi("https://x-clients-be.onrender.com")
db = StudentTable("postgresql:// postgres:19091947gG!@localhost:5432/tu_db")


# ТЕСТЫ
def test_get_student():
    """
    Проверяет количество студентов в API и в базе данных.
    """
    api_result = api.get_student_list()
    db_result = db.get_students()
    assert len(api_result) == len(db_result)


def test_get_active_student():
    """
    Проверяет активные записи через API и базу данных.
    """
    active_api_list = api.get_student_list(params_to_add={"active": "true"})
    active_db_list = db.get_active_students()
    assert len(active_api_list) == len(active_db_list)


def test_add_new():
    """
    Проверяет создание новой записи.
    """
    before_len = len(api.get_student_list())

    # Данные нового студента
    user_id = '007'
    level = 'Elementary'
    education_form = 'personal'
    subject_id = '5'

    # Создание нового студента через API
    result = api.create_student(
        user_id=user_id, level=level, education_form=education_form,
        subject_id=subject_id)
    new_id = result["id"]

    after_len = len(api.get_student_list())

    # Удаляем вновь созданного студента из базы данных
    db.delete_student(new_id)

    # Проверка, что новый студент действительно появился и имеет
    # нужные характеристики
    assert after_len - before_len == 1
    for student in api.get_student_list():
        if student["id"] == new_id:
            assert student["user_id"] == user_id
            assert student["level"] == level
            assert student["education_form"] == education_form
            assert student["subject_id"] == subject_id


def test_edit():
    """
    Проверяет редактирование существующего студента.
    """
    # Создаем нового студента
    initial_user_id = "007"
    db.create_student(initial_user_id)
    max_id = db.get_max_id()

    # Редактируем ученика через API
    new_user_id = "008"
    new_level = "Intermediate"
    new_education_form = "Group"
    new_subject_id = "2"

    edited = api.edit_student(
        student_id=max_id, user_id=new_user_id, level=new_level,
        education_form=new_education_form, subject_id=new_subject_id)

    # Удаляем отредактированную запись
    db.delete_student(max_id)

    # Проверяем, что изменения были применены корректно
    assert edited["id"] == max_id
    assert edited["user_id"] == new_user_id
    assert edited["level"] == new_level
    assert edited["education_form"] == new_education_form
    assert edited["subject_id"] == new_subject_id


def test_delete():
    """
    Проверяет удаление студента.
    """
    # Создаем нового студента
    user_id = "007"
    level = "Elementary"
    education_form = "Personal"
    subject_id = "1"
    db.create_student(user_id)
    max_id = db.get_max_id()

    # Удаляем через API
    deleted = api.delete_student(max_id)

    # Проверяем, что студент удалился
    assert deleted["id"] == max_id
    assert deleted["user_id"] == user_id
    assert deleted["level"] == level
    assert deleted["education_form"] == education_form
    assert deleted["subject_id"] == subject_id

    # Запрашиваем базу данных, проверяя, что удалённый
    # ученик больше не присутствует
    rows = db.get_student_by_id(max_id)
    assert len(rows) == 0


# from StudentApi import StudentApi
# from StudentTable import StudentTable

# api = StudentApi(не знаю где взять адрес)
# db = StudentTable(
#     "postgresql:// postgres:пароль@localhost:5432/moya_baza_2")


# def test_get_student():
#     api_result = api.get_student_list()
#     db_result = db.get_student()
#     assert len(api_result) == len(db_result)


# def test_get_active_student():
#     filtered_list = api.get_student_list(params_to_add={'active': 'true'})
#     db_list = db.get_active_student()
#     assert len(filtered_list) == len(db_list)


# def test_add_new():
#     body = api.get_student_list()
#     len_before = len(body)

#     name = "Alex"
#     level = "Elementary"
#     education_form = "personal"
#     subject_id = "1"
#     result = api.create_student(name, descr)
#     new_id = result["id"]

#     body = api.get_student_list()
#     len_after = len(body)
#     db.delete(new_id)

#     assert len_after - len_before == 1
#     for student in body:
#         if student["id"] == new_id:
#             assert student["name"] == name
#             assert student["level"] == level
#             assert student["education_form"] == education_form
#             assert student["subject_id"] == subject_id
#             assert student["id"] == new_id


# def test_edit():
#     name = 'Alex'
#     db. create(name)
#     max_id = db.get_max_id()
#     new_name = "Oleg"
#     new_level = "X"
#     new_education_form = "droup"
#     new_subject_id = "2"


#     edited = api.edit(max_id, new_name, new_descr)

#     db.delete(max_id)

#     assert edited["id"] == max_id
#     assert edited["name"] == new_name
#     assert edited["new_level"] == new_level
#     assert edited["new_education_form"] == new_education_form
#     assert edited["new_subject_id"] == new_subject_id
#     assert edited["isActive"] == True

# def test_delete():
#     name = 'Alex'
#     level = "Elementary"
#     education_form = "personal"
#     subject_id = "1"
#     db.create(name)
#     max_id = db.get_max_id()

#     deleted = api.delete(max_id)

#     assert deleted["id"] == max_id
#     assert deleted["name"] == name
#     assert deleted["level"] == level
#     assert deleted["education_form"] == education_form
#     assert deleted["subject_id"] == subject_id

#     assert deleted["isActive"] == True
#     rows = db.get_student_by_id(max_id)
#     assert len(rows) == 0
