# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Man:
    def __init__(self, surname, givenname):
        self.surname = surname
        self.givenname = givenname

    def __repr__(self):
        return '{} {}.'.format(self.surname, self.givenname[0])

class Class:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Класс: {}'.format(self.name)
    def add_student(self, student):
        self.add_students.add(student)

class Student(Man):
    def __init__(self, mother, father, *args):
        super(Student, self).__init__(*args)
        self.mother = mother
        self.father = father

class Parent(Man):
    def __init__(self, *args):
        super(Parent, self).__init__(*args)


class Teacher(Man):
    def __init__(self, classes, lesson, *args):
        super(Teacher, self).__init__(*args)
        self.classes = classes
        self.lesson = lesson

    def add_teacher(self, teacher):
        self.add_teacher.add(teacher)

    def add_teacher_lesson(self, lesson):
        self.add_teacher_lesson(lesson)

class School:
    def __init__(self):
        self.lessons = []
        self.classes = []
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_class(self, clazz):
        self.classes.append(clazz)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_teacher_lesson(self, lesson):
        self.lessons.append(lesson)

    def __repr__(self):
        return 'Школа, Классы: {}; Уроки:{}, Учителя:{}, Ученики: {}'.format(self.classes, self.lessons, self.teachers, self.students)


student = Student('Петрова', 'Петров', 'Петров', 'Олег')
teacher = Teacher('3Б', 'Математика', 'Суров', 'Иван')
clazz = Class('3а')
parent = Parent('Иванов', 'Иван')
school = School()
school.add_student(student)
school.add_class(clazz)
school.add_teacher(teacher)
school.add_teacher_lesson(teacher.lesson)
print(school)
print(parent)
