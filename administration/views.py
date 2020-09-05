from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.views.generic import DetailView
from .models import Notice, Student, User, Result, MyClassTeacher
from .decorators import student_required
from .forms import RegistrationForm, StudentForm, StudentLeaveApplicationForm
from account.models import Account
from teacher.models import Message, Grade
from account.forms import ResultForm

# Create your views here.
def home_page(request):
    grade = Grade.objects.all()
    notices = Notice.objects.all().order_by('-created_date')[:15]
    return render(request, 'administration/home.html', {'grade':grade, 'notices':notices})

@login_required
def class_notification(request, class_id):
    grade = Grade.objects.all()
    notification = Message.objects.all()
    if class_id:
        g = get_object_or_404(Grade, grade=class_id)
        notification = notification.filter(grade = g).order_by('-website')[0:1]
    context ={'g':g, 'notification' : notification, 'grade':grade}    
    return render(request, 'administration/class_notification.html', context)


def contact(request):
    return render(request, 'administration/contact.html')

def sports(request):
    return render(request, 'administration/sports.html')

def computer(request):
    return render(request, 'administration/computer.html')

def laboratory(request):
    return render(request, 'administration/laboratory.html')

def library(request):
    return render(request, 'administration/library.html')


def facilities(request):
    return render(request, 'administration/facilities.html')


def notice(request):
    notices = Notice.objects.all()
    return render(request, 'administration/notice.html', context={'notices':notices})


@login_required
@student_required
def student_form(request, id):
    grade = Grade.objects.all()
    if request.method == 'POST':
        pi = Student.objects.get(user = request.user.id)
        form = StudentForm(request.POST, instance = pi)
        if form.is_valid():
            form = StudentForm(request.POST, request.FILES, instance = pi)
            form.save()
            return redirect('/profile')   
    else:
        pi = Student.objects.get(user = request.user.id)
        form = StudentForm(instance = pi)
    return render(request, 'administration/student_form.html', {'form':form, 'grade':grade})



@student_required
def student_info(request):
    student = Student.objects.get(user = request.user.id)
    return render(request, 'administration/student_info.html', {'student':student})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request,"<h1>Page not found</h1>")    
    else:        
        return render(request, 'administration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


class NoticeDetailView(DetailView):
    model = Notice
    context_object = 'notice'
    template_name = 'administration/notice-detail.html'



def about(request):
    return render(request, 'administration/about.html')



@login_required
@student_required
def result(request):
    result = Result.objects.get(username = request.user.username)
    student = Student.objects.get(user = request.user.id)
    return render(request, 'administration/result.html', {'result':result, 'student':student})



def registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Registration Data Posted Successfully!')
            
    return render(request, 'administration/registration.html', {'form': form, 'messages':messages})     


@login_required
@student_required
def student(request):
    student = get_object_or_404(Student, user = request.user.id)
    return render(request, 'administration/student_profile.html',{'student':student})

@login_required
@student_required
def student_leave_form(request):
    form = StudentLeaveApplicationForm(request.POST or None)
    class_teacher = MyClassTeacher.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/success/')
    return render(request, 'administration/student_leave_form.html', {'form':form, 'class_teacher':class_teacher})


def success(request):
    return HttpResponse("<h1>Form Submitted Successfully</h1>")
