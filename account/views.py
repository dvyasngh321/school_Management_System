from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from administration.decorators import student_required, teacher_required, accountant_required
from .models import Account, Invoices, TeacherAccount
from .forms import AccountForm, TeacherAccountForm


@login_required
@accountant_required
def student_account(request):
    return render(request, 'account/student_account.html')

@login_required
@accountant_required
def account_page(request):
    form = AccountForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/account/information/')
    return render(request, 'account/account_page.html', {'form': form})


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


@login_required
@accountant_required
def invoice(request, id):
    invoice = Invoices.objects.all()
    if id:
        a = get_object_or_404(Account, pk = id)
        
        # invoice = invoice.filter(account = a)
    return render(request, 'account/invoice.html', {'invoice':invoice, 'a':a})

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
