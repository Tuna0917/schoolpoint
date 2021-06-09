from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True) #몇반 담임인지

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=32) #이름
    num = models.IntegerField() #번호
    point = models.IntegerField(default=0)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True) #반

    def __str__(self):
        return self.name


class Seat(models.Model):
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)


class Room(models.Model):
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)]) #학년
    num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(63)]) #반

    def __str__(self):
        return f"{self.grade}학년 {self.num}반"