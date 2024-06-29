from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from multiselectfield import MultiSelectField


class UserProfileProfessor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    age = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.first_name


class UserProfileStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.first_name


# Факультет
class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названия факультета')
    description = models.TextField(verbose_name='Описание факультета')

    def __str__(self):
        return self.name


# Профессор
class Professor(models.Model):
    user = models.OneToOneField(UserProfileProfessor, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Уроки')
    bio = models.TextField(verbose_name='Описания о профессоре')

    def __str__(self):
        return self.title


# Студент
class Student(models.Model):
    user = models.OneToOneField(UserProfileStudent, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField(verbose_name='В каком году началось учеба')
    graduation_date = models.DateField(verbose_name='В каком году закончиться учеба')


# Курс
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Поле для пароля роли

    def str(self):
        return self.name


class Course(AbstractUser):
    name = models.CharField(max_length=100, verbose_name='Названия курса')
    description = models.TextField(verbose_name='Описание о курсе')
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Измените related_name здесь
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Измените related_name здесь
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='user',
    )

    def __str__(self):
        return f'{self.department} - {self.professor} - {self.name}'


# Аудитория
class Room(models.Model):
    room_number = models.PositiveIntegerField(verbose_name='Аудитория')
    building_room = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    building = models.CharField(max_length=10, choices=building_room, verbose_name='Этаж')
    capacity = models.CharField(max_length=100, verbose_name='На сколько людей')

    def __str__(self):
        return f'{self.room_number} - {self.building_room}'


# Расписание
class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateField(verbose_name='Начало урока')
    end_time = models.DateField(verbose_name='Конец урока')
    day_of_week_choices = (
        ('понедельник', 'понедельник'),
        ('вторник', 'вторник'),
        ('среда', 'среда'),
        ('четверг', 'четверг'),
        ('пятница', 'пятница'),
        ('суббота', 'суббота'),
        ('воскресенье', 'воскресенье'),
    )
    day_of_week = MultiSelectField(max_length=100, choices=day_of_week_choices, verbose_name='Дни')

    def __str__(self):
        return f'{self.course} - {self.classroom}'


# Запись на курс
class Registration(models.Model):
    student = models.ForeignKey(UserProfileStudent, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.CharField(max_length=100)
    grade_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    grade = models.CharField(max_length=10, choices=grade_choices, default=0, verbose_name='Оценка')

    def __str__(self):
        return f'{self.course} - {self.student}'


# Домашнее задание
class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Имя задачи')
    description = models.TextField(verbose_name='Описание о задаче')
    due_date = models.CharField(max_length=100, verbose_name='До какого дня')

    def __str__(self):
        return f'{self.course} - {self.title}'


# Сдача домашнее задание
class Submitting(models.Model):
    assignment = models.CharField(max_length=100, verbose_name='Имя задачи')
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    submission_date = models.DateField(verbose_name='Дз тапшыруу')
    grade_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    grade = models.CharField(max_length=10, choices=grade_choices, verbose_name='Оценка')
    feedback = models.TextField('Отзывы о задаче')

    def __str__(self):
        return f'{self.assignment} - {self.student}'

