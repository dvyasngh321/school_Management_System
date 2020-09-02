from django.forms import ModelForm
from .models import AddClass, AddClassAsClassTeacher, Message

class AddClassForm(ModelForm):
    class Meta:
        model = AddClass
        fields = '__all__'

class AddClassAsClassTeacherForm(ModelForm):
    class Meta:
        model = AddClassAsClassTeacher
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'        