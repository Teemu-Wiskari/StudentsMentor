class Student:
    """
    Информация о студентах
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []  # список пройденных курсов
        self.courses_in_progress = []  # список курсов в процессе изучения
        self.grades_student = {}  # словарь оценок
        self.grades_average_hw = float()  # средний балл

    def rate_hw_lecturer(self, lecturer, course, grade):
        """
        Функция проверки объекта:
        - что он является экземпляром класса
        - закреплен за курсами, на которые подписан студент
        - и выставление оценок лекторам
        """
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached):

            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rating(self):
        """
        Функция, реализующая средний балл оценок студентов.
        """
        grades_count = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
        avg_rating = sum(map(sum, self.grades_student.values())) / grades_count

        return str(avg_rating)

    def __str__(self):
        """
        Вывод информации студента.
        """
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_rating()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Сравнить не возможно!")
            return

        return self.avg_rating > other.avg_rating


class Mentor:
    """
    Информация о менторах.
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # список прикрепленных курсов


class Lecturer(Mentor):
    """
    Наследованный класс лекторов.
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []  # список прикрепленных курсов
        self.grades_lecturer = {}  # словарь оценок лектора
        self.grades_average_lecture = []  # средняя оценка

    def __str__(self):
        """
        Функция, реализующая средний балл оценок лекторов и вывод информации лектора.
        """
        grades_count = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
        self.avg_rating = sum(map(sum, self.grades_lecturer.values())) / grades_count

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_rating}\n")

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнить не возможно!")
            return

        return self.avg_rating > other.avg_rating


class Reviewer(Mentor):
    """
    Наследованный класс экспертов.
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        """
        Функция проверки объекта:
        - что он является экземпляром класса
        - закреплен за курсами
        - и выставление оценок студентам
        """
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):

            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """
        Вывод информации эксперта.
        """

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


student_1 = Student('Teemu', 'Wiskari')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Aino', 'Tapio')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']


lecturer_1 = Lecturer('Emma', 'Virtanen')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Olivia', 'Korhonen')
lecturer_2.courses_attached += ['Python']


reviewer_1 = Reviewer('Johannes', 'Koskinen')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']


reviewer_1.rate_hw_student(student_1, 'Python', 8)
reviewer_1.rate_hw_student(student_1, 'Python', 5)
reviewer_1.rate_hw_student(student_1, 'Python', 3)
reviewer_1.rate_hw_student(student_1, 'Git', 6)
reviewer_1.rate_hw_student(student_1, 'Git', 8)

reviewer_1.rate_hw_student(student_2, 'Python', 3)
reviewer_1.rate_hw_student(student_2, 'Python', 8)
reviewer_1.rate_hw_student(student_2, 'Python', 9)
reviewer_1.rate_hw_student(student_2, 'Git', 9)
reviewer_1.rate_hw_student(student_2, 'Git', 5)


student_1.rate_hw_lecturer(lecturer_1, 'Python', 8)
student_1.rate_hw_lecturer(lecturer_1, 'Python', 4)
student_1.rate_hw_lecturer(lecturer_1, 'Python', 9)
student_1.rate_hw_lecturer(lecturer_1, 'Git', 10)
student_1.rate_hw_lecturer(lecturer_1, 'Git', 9)

student_2.rate_hw_lecturer(lecturer_2, 'Python', 5)
student_2.rate_hw_lecturer(lecturer_2, 'Python', 9)
student_2.rate_hw_lecturer(lecturer_2, 'Python', 7)
student_1.rate_hw_lecturer(lecturer_1, 'Git', 8)
student_1.rate_hw_lecturer(lecturer_1, 'Git', 6)

print(f"Проверяющий:\n{reviewer_1}")
print(f"Студенты:\n{student_1}\n{student_2}")
print(f"Лекторы:\n{lecturer_1}\n{lecturer_2}")
