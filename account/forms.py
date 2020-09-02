from django.forms import ModelForm
from .models import Invoices, Account, TeacherAccount
from administration.models import Result


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class TeacherAccountForm(ModelForm):
    class Meta:
        model = TeacherAccount
        fields = '__all__'

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = '__all__'        