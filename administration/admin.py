from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import (User, Student, Teacher, Registration, Accountant, MyClassTeacher, Notice, Result, 
                          TeacherLeaveApplication,Contact,ApplyForExamination, StudentLeaveApplication,
                          Comment, Post, Event, Principal, Gallery, PublishResult)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_date']

admin.site.register(PublishResult)
admin.site.register(ApplyForExamination)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Notice)
admin.site.register(Teacher)
admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Accountant)
admin.site.register(MyClassTeacher)
admin.site.register(Result)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Principal)

class StudentLeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ['student','teacher_username', 'created_date']
    search_fields = ['student','teacher_username', 'created_date']

admin.site.register(StudentLeaveApplication, StudentLeaveApplicationAdmin)

class TeacherLeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_date']
    search_fields = ['user', 'created_date']

admin.site.register(TeacherLeaveApplication, TeacherLeaveApplicationAdmin)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username':"This Username has already been taken!"
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_message['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = AuthUserAdmin.fieldsets + (
        ('Extended Fields', {'fields': ('is_student', 'is_teacher','is_accountant', 'is_classteacher', 'is_principal')}),
    )
    list_display = ('username', 'is_student', 'is_teacher', 'is_accountant', 'is_classteacher', 'is_superuser', 'is_principal')
    search_fields = ['username']


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name']

admin.site.register(Registration,RegistrationAdmin)