class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.grades}\n" \
               f"Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

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
                grade_list += grade
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
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}"

    def get_average_grade(self):
        grade_list = []
        for course in self.grades:
            for grade in self.grades[course]:
                grade_list += grade
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


#
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_studasdasdent = Student('Ruoy', 'Eman', 'your_gender')


print(best_student.get_average_grade() >= best_studasdasdent.get_average_grade())
# best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Python']
#
print(best_student)
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 6)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 8)
#
# print(best_student.grades)
#
