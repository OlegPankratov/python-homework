class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        print(isinstance(student, Student))
        print(course in self.courses_attached)
        print(course in student.courses_in_progress)
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer():
    ...

class Reviewer(Mentor):
    ...

ivan_student = Student('Иван', 'Иванов', 'м')
cidr_student = Student('Сидр', 'Сидоров', 'м')


# ivan_student.finished_courses = ['Python']
# ivan_student.courses_in_progress += ['Python']
# cidr_student.courses_in_progress += ['Python']
print(ivan_student.finished_courses)

fedor = Lecturer()

#
pen = Mentor('Some', 'Buddy')
print(pen.rate_hw(cidr_student, 'Python', 5))

# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
bnbnbnbbn
