class Student:
    """
    Информация о студентах
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # список пройденных курсов
        self.courses_in_progress = []  # список курсов в процессе изучения
        self.grades_student = {}  # словарь оценок

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
        result = sum(map(sum, self.grades_student.values())) / grades_count

        return result

    def avg_rating_course(self, course):
        """
        Функция, реализующая средний балл оценок за курс.
        """
        sum_course = 0
        len_course = 0
        for crs in self.grades_student.keys():
            if crs == course:
                sum_course += sum(self.grades_student[course])
                len_course += len(self.grades_student[course])
        result = round(sum_course / len_course, 2)
        return result

    def __str__(self):
        """
        Вывод информации студента.
        """
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Пол: {self.gender}\n"
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
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []  # список прикрепленных курсов


class Lecturer(Mentor):
    """
    Наследованный класс лекторов.
    """
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
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
                f"Пол: {self.gender}\n"
                f"Средняя оценка за лекции: {self.avg_rating}\n")

    def avg_rating_course(self, course):
        """
        Функция, реализующая средний балл оценок за курс.
        """
        sum_course = 0
        len_course = 0
        for crs in self.grades_lecturer.keys():
            if crs == course:
                sum_course += sum(self.grades_lecturer[course])
                len_course += len(self.grades_lecturer[course])
        result = round(sum_course / len_course, 2)
        return result

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнить не возможно!")
            return

        return self.avg_rating > other.avg_rating


class Reviewer(Mentor):
    """
    Наследованный класс экспертов.
    """
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)

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
                f"Фамилия: {self.surname}\n"
                f"Пол: {self.gender}\n")


# Студенты
student_1 = Student('Teemu', 'Wiskari', 'Man')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['JavaScript']

student_2 = Student('Aino', 'Tapio', 'Woman')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['C++']

# Лекторы
lecturer_1 = Lecturer('Emma', 'Virtanen', 'Woman')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Olivia', 'Korhonen', 'Woman')
lecturer_2.courses_attached += ['Python', 'Git']

# Эксперты
reviewer_1 = Reviewer('Johannes', 'Koskinen', 'Man')
reviewer_1.courses_attached += ['Python', 'Git']

# Оценки экспертов
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 8)
reviewer_1.rate_hw_student(student_1, 'Python', 6)
reviewer_1.rate_hw_student(student_1, 'Git', 7)
reviewer_1.rate_hw_student(student_1, 'Git', 5)

reviewer_1.rate_hw_student(student_2, 'Python', 4)
reviewer_1.rate_hw_student(student_2, 'Python', 8)
reviewer_1.rate_hw_student(student_2, 'Python', 7)
reviewer_1.rate_hw_student(student_2, 'Git', 9)
reviewer_1.rate_hw_student(student_2, 'Git', 8)

# Оценки студентов
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

# Вывод информации
print(f"Проверяющий:\n{reviewer_1}")
print(f"Студенты:\n{student_1}\n{student_2}")
print(f"Лекторы:\n{lecturer_1}\n{lecturer_2}")

# Список студентов и лекторов
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]


def avg_rate_course_student(course, students):
    """
    Функция, для подсчета средней оценки студента за домашние задания
    """
    sum = 0
    qty = 0
    for student in students:
        student_sum_rate = student.avg_rating_course(course)
        sum += student_sum_rate
        qty += 1
    result = round(sum / qty, 2)
    return result


def avg_rate_course_lecturer(course, lecturers):
    """
    Функция, для подсчета средней оценки лектора за лекцию
    """
    sum = 0
    qty = 0
    for lecturer in lecturers:
        lecturer_sum_rate = lecturer.avg_rating_course(course)
        sum += lecturer_sum_rate
        qty += 1
    result = round(sum / qty, 2)
    return result


print('Подсчет средней оценки за домашние задания студентов')
print(avg_rate_course_student('Git', students))

print('Подсчет средней оценки за лекции лекторов')
print(avg_rate_course_lecturer('Python', lecturers))
