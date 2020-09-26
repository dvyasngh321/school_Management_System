from django.forms import ModelForm
from .models import Account, TeacherAccount, Expense,Payment
from administration.models import Result


class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('id', 'total',)

class TeacherAccountForm(ModelForm):
    class Meta:
        model = TeacherAccount
        exclude = ('id','tax',)

class ResultForm(ModelForm):
    class Meta:
        model = Result
        exclude = ('total', 'percentage')



class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['source', 'amount']

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ('account',)        