from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True) #몇반 담임인지

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS = (
        ('a', '재학'), #Attending
        ('b', '휴학'), #Break
        ('d', '자퇴'), #Dropout
        ('k', '퇴학') #Kicked
    )
    name = models.CharField(max_length=32) #이름
    num = models.IntegerField(validators=[MinValueValidator(1),]) #번호
    point = models.IntegerField(default=0,validators=[MinValueValidator(0),])
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True) #반
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='a'
    )


    def __str__(self):
        return self.name


class Seat(models.Model):
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)


class Room(models.Model):
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)]) #학년
    num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(63)]) #반
    line = models.IntegerField(validators=[MinValueValidator(1),])

    def __str__(self):
        return f"{self.grade}학년 {self.num}반"

class SeatLog(models.Model):
    date = models.DateTimeField(auto_now_add=True) #언제
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING) #누가
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE) #어떤 좌석을
    points = models.IntegerField(validators=[MinValueValidator(0),]) #얼마에