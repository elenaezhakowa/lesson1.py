from StudentApi import StudentApi
from StudentTable import StudentTable

api = StudentApi(не знаю где взять адрес)
db = StudentTable(
    "postgresql:// postgres:19091947gG!@localhost:5432/moya_baza_2")


def test_get_student():
    api_result = api.get_student_list()
    db_result = db.get_student()
    assert len(api_result) == len(db_result)


def test_get_active_student():
    filtered_list = api.get_student_list(params_to_add={'active': 'true'})
    db_list = db.get_active_student()
    assert len(filtered_list) == len(db_list)


def test_add_new():
    body = api.get_student_list()
    len_before = len(body)

    name = "Alex"
    level = "Elementary"
    education_form = "personal"
    subject_id = "1"
    result = api.create_student(name, descr)
    new_id = result["id"]

    body = api.get_student_list()
    len_after = len(body)
    db.delete(new_id)

    assert len_after - len_before == 1
    for student in body:
        if student["id"] == new_id:
            assert student["name"] == name
            assert student["level"] == level
            assert student["education_form"] == education_form
            assert student["subject_id"] == subject_id
            assert student["id"] == new_id


def test_edit():
    name = 'Alex'
    db. create(name)
    max_id = db.get_max_id()
    new_name = "Oleg"
    new_level = "X"
    new_education_form = "droup"
    new_subject_id = "2"


    edited = api.edit(max_id, new_name, new_descr)

    db.delete(max_id)

    assert edited["id"] == max_id
    assert edited["name"] == new_name
    assert edited["new_level"] == new_level
    assert edited["new_education_form"] == new_education_form
    assert edited["new_subject_id"] == new_subject_id
    assert edited["isActive"] == True

def test_delete():
    name = 'Alex'
    level = "Elementary"
    education_form = "personal"
    subject_id = "1"
    db.create(name)
    max_id = db.get_max_id()

    deleted = api.delete(max_id)

    assert deleted["id"] == max_id
    assert deleted["name"] == name
    assert deleted["level"] == level
    assert deleted["education_form"] == education_form
    assert deleted["subject_id"] == subject_id
   
    assert deleted["isActive"] == True
    rows = db.get_student_by_id(max_id)
    assert len(rows) == 0
