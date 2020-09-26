from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from administration.decorators import student_required, teacher_required, accountant_required
from administration.models import ApplyForExamination
from administration.forms import ApplyForExaminationForm
from .models import Account, TeacherAccount, Expense, Payment
from .forms import AccountForm, TeacherAccountForm, ExpenseForm, PaymentForm


@login_required
@accountant_required
def student_account(request):
    return render(request, 'account/student_account.html')
  


def expense(request):
    expense = Expense.objects.all()
    form = ExpenseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            form = ExpenseForm()
    return render(request, 'account/expense.html', {'expense':expense, 'form':form})            


@login_required
@accountant_required
def account_page(request):
    form = AccountForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/account/information/')
    return render(request, 'account/account_page.html', {'form': form})

def view_Payment(request, id):
    account = Account.objects.get(id = id)
    payment = Payment.objects.filter(account = account).order_by('-created_date')
    return render(request, 'account/view_payment.html', {'payment': payment, 'account':account})

@login_required
@accountant_required
def teacher_account_form(request):
    form = TeacherAccountForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/account/teacher_account_detail')    
    return render(request, 'account/teacher_account_form.html', {'form': form})

@login_required
@accountant_required
def teacher_account_detail(request):
    account = TeacherAccount.objects.all()
    return render(request, 'account/teacher_account_detail.html', {'account':account})

@login_required
@accountant_required
def update_teacher_data(request, id):
    if request.method == 'POST':
        pi = TeacherAccount.objects.get(pk = id)
        form = TeacherAccountForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('/account/teacher_account_detail/')
    else:
        pi = TeacherAccount.objects.get(pk=id)
        form = TeacherAccountForm(instance = pi)
    return render(request, 'account/update_teacher_account.html', {'form':form})

def approve_student_for_exam(request):
    student = ApplyForExamination.objects.all().order_by('-created_date')
    return render(request, 'account/approve_form.html', {'student':student})

def delete_all(request):
    if request.method == 'POST':
        all = ApplyForExamination.objects.all()
        all.delete()
        return redirect('/success/')

def confirm_approval(request, id):    
    if request.method == 'POST':
        pi = ApplyForExamination.objects.get(pk = id)
        form = ApplyForExaminationForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        pi = ApplyForExamination.objects.get(pk=id)
        form = ApplyForExaminationForm(instance = pi)
    return render(request, 'account/confirm.html', {'form':form})



@login_required
@accountant_required
def delete_teacher_data(request, id):
    if request.method == 'POST':
        pi = TeacherAccount.objects.get(pk=id)
        pi.delete()
        return redirect('/account/teacher_account_detail/')


@login_required
@accountant_required
def account_information(request):
    account = Account.objects.all()
    return render(request, 'account/account_information.html', {'account':account})


def payment(request, id):
    account = Account.objects.get(pk=id)
    print(account)
    form = PaymentForm(request.POST or None)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        paid = request.POST.get('paid')
        remaining = request.POST.get('remaining')
        discount = request.POST.get('discount')
        cheque = request.POST.get('cheque')
        cash = request.POST.get('cash')
        online_banking = request.POST.get('online_banking')
        if cash == 'on':
            cash = True
        else:
            cash = False    
        if cheque == 'on':
            cheque = True
        else:
            cheque = False    
        if online_banking == 'on':
            online_banking = True
        else:
            online_banking = False     
        payment = Payment.objects.create(account=account, amount = amount, paid = paid, discount=discount, cash=cash, remaining=remaining, cheque=cheque, online_banking=online_banking)
        payment.save()
        return HttpResponseRedirect(reverse('view_payment', args=(id,)))
    return render(request, 'account/payment.html', {'account':account, 'form':form})        

@login_required
@accountant_required
def invoice(request, id):
    a = get_object_or_404(Account, pk = id)
    return render(request, 'account/invoice.html', {'a':a})


@login_required
@accountant_required
def search(request):
    q = request.GET['query']
    account = Account.objects.filter(student__icontains = q)
    return render(request, 'account/search.html', {'q':q, 'account':account})


@login_required
@accountant_required
def paybill(request, id):
    paybill = TeacherAccount.objects.get(pk=id)
    if id:
        a = get_object_or_404(TeacherAccount, pk = id)
    return render(request, 'account/paybill.html', {'paybill': paybill, 'a':a})

@login_required
@accountant_required
def update_information(request, id):
    if request.method == 'POST':
        pi = Account.objects.get(pk = id)
        form = AccountForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('/account/information/')
    else:
        pi = Account.objects.get(pk=id)
        form = AccountForm(instance = pi)
    return render(request, 'account/update_student_account.html', {'form':form})    

@login_required
@accountant_required
def delete_information(request, id):
    if request.method == 'POST':
        pi = Account.objects.get(pk=id)
        pi.delete()
        return redirect('/account/')
