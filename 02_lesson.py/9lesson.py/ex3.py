from student import Student
from course_group import CourseGroup

student = Student("Вася", "Иванов", 20, "инженер")
classmate1 = Student("Иван", "Петров", 27, "Инженер по тестированию")
classmate2 = Student("Мария", "Сидорова", 24, "Инженер по тестированию")
classmate3 = Student("Дмитрий", "Кузнецов", 26, "Инженер по тестированию")


course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
# Выводим информацию о группе
print(course_group)
