from django.forms import ModelForm
from .models import Registration, Student

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'