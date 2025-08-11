import requests


class StudentApi:
    def __init__(self, url):
        self.url = url

    def get_student_list(self, params_to_add=None):
        response = requests.get(f'{self.url}/students', params=params_to_add)
        return response.json()

    def create_student(self, user_id, level, education_form, subject_id):
        data = {
            "user_id": user_id,
            "level": level,
            "education_form": education_form,
            "subject_id": subject_id
        }
        response = requests.post(f'{self.url}/students', json=data)
        return response.json()

    def edit_student(
            self, student_id, user_id, level, education_form, subject_id):
        data = {
            "user_id": user_id,
            "level": level,
            "education_form": education_form,
            "subject_id": subject_id
        }
        response = requests.put(f'{self.url}/students/{student_id}', json=data)
        return response.json()

    def delete_student(self, student_id):
        response = requests.delete(f'{self.url}/students/{student_id}')
        return response.json()

# import requests
# class StudentApi:
#     # Инициализация
#     def __init__(self, url) -> None:
#         self.url = url

#     def set_active_state(self, id, is_active):
#         client_token = self.get_token()

#         url_with_token = f"""
# {self.url}/company/status_update/{id}?client_token={client_token}"""
#         resp = requests.patch(url_with_token, json={"is_active": is_active})
#         return resp.json()

#     def get_student_list(self, params_to_add=None):
#         """
#         Получаем список студентов через API.

#         :param params_to_add: Дополнительные параметры для фильтрации списка.
#         :return: Список студентов.
#         """
#         response = requests.get(f'{self.url}/students', params=params_to_add)
#         return response.json()
