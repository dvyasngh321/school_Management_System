from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User, Student, Teacher, Registration, Accountant, MyClassTeacher, Notice, Result
admin.site.register(Notice)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Accountant)
admin.site.register(MyClassTeacher)
admin.site.register(Result)

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
        ('Extended Fields', {'fields': ('is_student', 'is_teacher','is_accountant', 'is_classteacher')}),
    )
    list_display = ('username', 'is_student', 'is_teacher', 'is_accountant', 'is_classteacher', 'is_superuser')
    search_fields = ['username']


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name']

admin.site.register(Registration,RegistrationAdmin)    