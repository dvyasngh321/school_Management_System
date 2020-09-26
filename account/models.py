from django.db import models
from administration.models import User, Teacher, Student
from teacher.models import Grade


class Account(models.Model):
    id = models.IntegerField(primary_key = True)
    user = models.OneToOneField(Student,on_delete=models.CASCADE)
    student = models.CharField(max_length=250)
    grade = models.ForeignKey(Grade, on_delete = models.CASCADE)
    month = models.CharField(max_length=40)
    month_count = models.IntegerField(default = 1)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True ,null=True)
    bus_fee = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)
    laboratory_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    miscellaneous = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places = 2)
    remaining = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places = 2, default = 0.00, blank=True, null=True)
    description = models.CharField(max_length=1000)
    paid = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)

    
    def save(self):
        if self.paid == False:
            self.amount = self.laboratory_fee + self.tuition_fee * self.month_count + self.bus_fee * self.month_count + self.miscellaneous
            self.total = float(self.amount) + float(self.remaining)
        else:
            self.bus_fee = 0.00
            self.miscellaneous = 0.00
            self.tuition_fee = 0.00
            self.laboratory_fee = 0.00
            self.amount = 0.00
            self.total = float(self.amount) + float(self.remaining)
        return super(Account, self).save()    


    def __str__(self):
        return self.student

class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)
    paid = models.DecimalField(max_digits=10, decimal_places=2)
    remaining = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null =True)
    cash = models.BooleanField(default = False)
    cheque = models.BooleanField(default=False)
    online_banking = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add =True)

    def save(self, *args, **kwargs):
        self.remaining = float(self.amount) - float(self.discount) - float(self.paid)       
        return super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return self.account.student



class TeacherAccount(models.Model):
    id = models.IntegerField(primary_key = True)
    Staff_Username = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    tax = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    paid = models.BooleanField(default=False)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self):
        if self.salary * 12 >= 480000:
            self.tax = float(self.salary) * 12 * 0.13
            self.tax = float(self.tax) / 12
        else:
            self.tax = 0.00
        return super(TeacherAccount, self).save()             

    def __str__(self):
        return self.name



class Expense(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=2000)
    amount = models.DecimalField(max_digits=100, decimal_places=3)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.source      
        