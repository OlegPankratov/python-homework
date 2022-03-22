class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{round(self.get_average_grade(), 1)}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

    def rate_hw(self, lecturer, course, grade):
        course_exists = course in self.courses_in_progress and course in lecturer.courses_attached
        if isinstance(lecturer, Lecturer) and course_exists and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        grade_list = []
        for course in self.grades:
            for grade in self.grades[course]:
                grade_list += [grade]
        if len(grade_list) == 0:
            average_grade = 0
        else:
            average_grade = sum(grade_list) / len(grade_list)
        return average_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.get_average_grade(), 1)}"

    def get_average_grade(self):
        grade_list = []
        for course in self.grades:
            for grade in self.grades[course]:
                grade_list += [grade]
        if len(grade_list) == 0:
            average_grade = 0
        else:
            average_grade = sum(grade_list) / len(grade_list)
        return average_grade

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Иван', 'Иванов', 'муж.')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование', 'Git']

best1_student = Student('Александра', 'Александрова', 'жен.')
best1_student.courses_in_progress += ['Python']
best1_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Виктор', 'Викторов')
cool_lecturer.courses_attached += ['Python']

cool1_lecturer = Lecturer('Елена', 'Семенова')
cool1_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Сергей', 'Сергеев')
cool_reviewer.courses_attached += ['Python']

cool1_reviewer = Reviewer('Василиса', 'Васильева')
cool1_reviewer.courses_attached += ['Python']

cool1_reviewer.rate_hw(best_student, 'Python', 9)
cool1_reviewer.rate_hw(best_student, 'Python', 10)
cool1_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(best1_student, 'Python', 10)
cool_reviewer.rate_hw(best1_student, 'Python', 9)
cool_reviewer.rate_hw(best1_student, 'Python', 10)

best_student.rate_hw(cool1_lecturer, 'Python', 9)
best1_student.rate_hw(cool1_lecturer, 'Python', 10)

best_student.rate_hw(cool_lecturer, 'Python', 10)
best1_student.rate_hw(cool_lecturer, 'Python', 10)

print(best_student)
print('------------')
print(best1_student)
print('------------')
print(cool_lecturer)
print('------------')
print(cool1_lecturer)
print('------------')
print(cool_reviewer)
print('------------')
print(cool1_reviewer)
print('------------')

