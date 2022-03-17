
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
            f"Курсы в процессе изучения:{courses_in_progress_str}\nЗавершенные курсы:{finished_courses_str}"
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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Tom', 'Candy')
cool_lecturer.courses_attached += ['Python']
 
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 10)

print(best_student.grades)
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
