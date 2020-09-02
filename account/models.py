from django.db import models
from administration.models import User, Teacher, Student


class Account(models.Model):
    id = models.IntegerField(primary_key = True)
    user = models.OneToOneField(Student,on_delete=models.CASCADE)
    student = models.CharField(max_length=250)
    grade = models.CharField(max_length=40)
    month = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places = 2)
    total = models.DecimalField(max_digits=10, decimal_places = 2, default = 0.00)
    paid = models.DecimalField(max_digits=10, decimal_places = 2, blank = True, null=True)
    remaining_due = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student


class Invoices(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account.student


class TeacherAccount(models.Model):
    id = models.IntegerField(primary_key = True)
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    paid = models.BooleanField(default=False)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


        