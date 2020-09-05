from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from teacher.models import Grade

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_classteacher = models.BooleanField(default=False)

gender_choices = (('Male', 'Male'), ('Female', 'Female'))


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length = 100, blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)
    gender = models.CharField(max_length=10, choices = gender_choices, default='Male')
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=2000)
    dob = models.DateField(default="1990-8-12")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    gender = models.CharField(max_length=10, choices = gender_choices, default='Male')
    phone = models.CharField(max_length=100, default=123)
    location = models.CharField(max_length=100, default=23)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
 
    def __str__(self):
        return self.user.username


class Accountant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices = gender_choices, default='Male')
    phone = models.CharField(max_length=100, default=123)
    location = models.CharField(max_length=100, default=23)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.username


class MyClassTeacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices = gender_choices, default='Male')
    phone = models.CharField(max_length=100, default=123)
    location = models.CharField(max_length=100, default=23)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Notice(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now= True, blank=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(blank = True, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    grade = models.IntegerField()
    voucher = models.ImageField(upload_to='images', blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Result(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    class_teacher_id = models.ForeignKey(MyClassTeacher,on_delete=models.CASCADE)
    math = models.DecimalField(max_digits=10, decimal_places= 2)
    English = models.DecimalField(max_digits=10, decimal_places= 2)
    social_studies = models.DecimalField(max_digits=10, decimal_places= 2)
    science = models.DecimalField(max_digits=10, decimal_places= 2)
    nepali = models.DecimalField(max_digits=10, decimal_places= 2)
    population = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank = True)

    def __str__(self):
        return self.username

class StudentLeaveApplication(models.Model):
    student = models.CharField(max_length=100)
    teacher_username = models.CharField(max_length=200)
    reason = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reason


class TeacherLeaveApplication(models.Model):
    user = models.CharField(max_length=200)
    reason = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_student:
        Student.objects.get_or_create(user=instance)
    elif instance.is_teacher:
        Teacher.objects.get_or_create(user=instance)
    elif instance.is_accountant:
        Accountant.objects.get_or_create(user=instance)
    elif instance.is_classteacher:
        MyClassTeacher.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_student:
        instance.student.save()
    elif instance.is_teacher:
        instance.teacher.save()
    elif instance.is_accountant:
        instance.accountant.save()
    elif instance.is_classteacher:
        instance.myclassteacher.save()        
