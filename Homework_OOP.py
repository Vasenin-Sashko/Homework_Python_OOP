
from unittest import result


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating_hw = float()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_student:
                lecturer.grades_student[course] += [grade]
            else:
                lecturer.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sum_grade = 0
        numb = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        for value in self.grades.values():
            for elemant in value:
                sum_grade += elemant
                numb +=1
        self.average_rating_hw = sum_grade/numb
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating_hw}\n" \
            f"Курсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение!')
            return
        return self.average_rating_hw < other.average_rating_hw


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)        
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_student = {}
        self.average_rating = float()

    def __str__(self):
        sum_grade = 0
        numb = 0
        for value in self.grades_student.values():
            for elemant in value:
                sum_grade += elemant
                numb +=1
        self.average_rating = sum_grade/numb
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}"
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение!')
            return
        return self.average_rating < other.average_rating

# Экземпляры класса "Student":
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

student_1 = Student('Andy', 'Anderson', 'man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['js']

student_2 = Student('Kate', 'Cooper', 'woman')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программироание']

# Экземпляры класса "Reviewer":
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

reviewer_1 = Reviewer('Alex', 'Holmes')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Mary', 'Holmes')
reviewer_2.courses_attached += ['Python']

# Экземпляры класса "Lecturer":
cool_lecturer = Lecturer('Tom', 'Candy')
cool_lecturer.courses_attached += ['Python']

lecturer_1 = Lecturer('Harry', 'Potter')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Jerry', 'Blue')
lecturer_2.courses_attached += ['Python']

# Оценки экспертов:
cool_reviewer.rate_hw(student_1, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(student_2, 'Python', 9)

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(best_student, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)

# Оценки студентов:
best_student.rate_lecture(lecturer_1, 'Python', 7)
best_student.rate_lecture(lecturer_2, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 10)

student_1.rate_lecture(cool_lecturer, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_2, 'Python', 8)

student_2.rate_lecture(cool_lecturer, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 5)
student_2.rate_lecture(lecturer_2, 'Python', 7)

# Список студентов, лекторов и экспертов:
print(f'Список студентов:\n\n{student_1}\n\n{student_2}\n\n{best_student}')
print()
print(f'Список лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{cool_lecturer}')
print()
print(f'Список экспертов:\n\n{reviewer_1}\n\n{reviewer_2}\n\n{cool_reviewer}')
print()
print()

# Сравнение студентов по средним оценкам за домашние задания:
print(f'Результат сравнения студентов по средним оценкам за ДЗ: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')

# Сравнение студентов по средним оценкам за домашние задания:
print(f'Результат сравнения лекторов по средним оценкам за лекции: '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 < lecturer_2}')
print()

# Реализация функций средних оценок за ДЗ у студентов и средних оценок за лекции у лекторов:
student_list = [student_1, student_2, best_student]
lecturer_list = [lecturer_1, lecturer_2, cool_lecturer]

def student_rating(student_list, course):
    sum_grade = 0
    numb = 0
    for person in student_list:
        if person.courses_in_progress == [course]:
            sum_grade += person.average_rating_hw
            numb +=1
        general_rating = sum_grade/numb
        return general_rating

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

def lecturer_rating(lecturer_list, course):
    sum_grade = 0
    numb = 0
    for person in lecturer_list:
        if person.courses_attached == [course]:
            sum_grade += person.average_rating
            numb +=1
        general_rating = sum_grade/numb
        return general_rating

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()