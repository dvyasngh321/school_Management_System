from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from administration.models import User, Teacher, StudentLeaveApplication
from administration.decorators import teacher_required, classteacher_required, teachers_required
from .forms import AddClassForm, AddClassAsClassTeacherForm, MessageForm
from .models import AddClass, AddClassAsClassTeacher
from administration.models import Student, MyClassTeacher, Result
from account.forms import ResultForm

@login_required
@teachers_required
def teacher_page(request):
    user = User.objects.get(id = request.user.id)
    mygrade = AddClassAsClassTeacher.objects.filter(username = request.user.username)
    return render(request, 'teacher/teacher_page.html', {'mygrade':mygrade})

@login_required
@teachers_required
def add_class_notification(request):
    form = MessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/success')
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
            return redirect('/teacher/')
    return render(request, "teacher/class_teacher_form.html", {'form': form})


@login_required
@teachers_required
def manage_result(request, class_id):
    form = ResultForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage_result', args=(class_id,)))
    result = Result.objects.filter(class_teacher_id = request.user.id)
    for instance in result:
        instance.total = instance.math + instance.science + instance.social_studies + instance.population + instance.English + instance.nepali
        instance.percentage = (instance.total/6)
        instance.save()
    return render(request, 'teacher/manage_result.html', {'form':form, 'result':result})


@login_required
@classteacher_required
def update_result(request, id):
    if request.method == 'POST':
        pi = Result.objects.get(pk=id)
        form = ResultForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage_result',args=(pi,)))
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
        return HttpResponseRedirect(reverse('manage_result', args =(pi,)))


@login_required
@teachers_required
def leave_notifications(request):
    leave_notifications = StudentLeaveApplication.objects.filter(teacher_username = request.user.username).order_by('-created_date')
    return render(request, 'teacher/leave_notifications.html', {'leave_notifications':leave_notifications})


@login_required
@classteacher_required
def delete_leave_notification(request, id):
    if request.method == 'POST':
        notification = StudentLeaveApplication.objects.get(id = id)
        notification.delete()
        return redirect('/teacher/leave_notification/')
