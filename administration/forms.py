from django.forms import ModelForm
from .models import Registration, Student, StudentLeaveApplication, ApplyForExamination,TeacherLeaveApplication,Post, Comment, Contact

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'        

class StudentLeaveApplicationForm(ModelForm):
    class Meta:
        model = StudentLeaveApplication
        exclude = '__all__'


class TeacherLeaveApplicationForm(ModelForm):
    class Meta:
        model = TeacherLeaveApplication
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)

class ApplyForExaminationForm(ModelForm):
    class Meta:
        model = ApplyForExamination
        fields = '__all__'