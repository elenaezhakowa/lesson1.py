class Student:
    def __init__(self, first_name, last_name, age, course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course

    def _str_(self):
        return (
            f"{self.first_name} {self.last_name}, "
            f"{self.age} лет, курс: {self.course}"
        )
