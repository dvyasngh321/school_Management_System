from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from administration.models import User
from administration.decorators import teacher_required, classteacher_required, teachers_required
from .forms import AddClassForm, AddClassAsClassTeacherForm, MessageForm
from .models import AddClass, AddClassAsClassTeacher
from administration.models import Student, MyClassTeacher, Result
from account.forms import ResultForm

@login_required
@teacher_required
def teacher_page(request):
    user = User.objects.get(id = request.user.id)
    myclass = AddClass.objects.filter(username = user)
    form = AddClassForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'teacher/teacher_page.html', {'myclass':myclass,'form':form})

@login_required
@teachers_required
def add_class_notification(request):
    form = MessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'teacher/add_notification_for_class.html', {'form':form})        

@login_required
@classteacher_required
def class_teacher_page(request):
    form1 = AddClassForm(request.POST or None)
    teacher = User.objects.get(username = request.user.username)
    myclass = AddClass.objects.filter(username = teacher)
    mygrade = AddClassAsClassTeacher.objects.filter(username = request.user.username)
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
    return render(request, 'teacher/class_teacher_page.html', {'form1': form1, 'myclass':myclass, 'mygrade':mygrade})


@login_required
@classteacher_required
def add_your_class(request):
    form = AddClassAsClassTeacherForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, "teacher/class_teacher_form.html", {'form': form})


@login_required
@classteacher_required
def manage_result(request, class_id):
    form = ResultForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    if class_id:
        result = Result.objects.filter(class_teacher_name = request.user.username)
        student = Student.objects.filter(grade = class_id)
        return render(request, 'teacher/manage_result.html', {'student':student, 'form':form, 'result':result})

@login_required
@classteacher_required
def update_result(request, id):
    if request.method == 'POST':
        pi = Result.objects.get(pk = id)
        form = ResultForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('/teacher/classteacher/')
    else:
        pi = Result.objects.get(pk=id)
        form = ResultForm(instance = pi)
    return render(request, 'teacher/update_result.html', {'form':form})


@login_required
@classteacher_required
def delete_result(request, id):
    if request.method == 'POST':
        pi = Result.objects.get(pk=id)
        pi.delete()
        return redirect('/teacher/classteacher/')


@login_required
@teachers_required
def attendance(request, class_id):
    if class_id:
        student = Student.objects.filter(grade = class_id)
        return render(request, 'teacher/take_attendance.html', {'student':student})        