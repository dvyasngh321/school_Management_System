from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.views.generic import DetailView
from .models import Notice, Student, User
from .decorators import student_required
from .forms import RegistrationForm, StudentForm
from account.models import Account
from teacher.models import Message, Grade
from account.forms import ResultForm

# Create your views here.
def home_page(request):
    grade = Grade.objects.all()
    notices = Notice.objects.all()
    return render(request, 'administration/home.html', {'grade':grade, 'notices':notices})

@login_required
def class_notification(request, class_id):
    grade = Grade.objects.all()
    notification = Message.objects.all()
    if class_id:
        g = get_object_or_404(Grade, grade=class_id)
        notification = notification.filter(grade = g)
    context ={'g':g, 'notification' : notification, 'grade':grade}    
    return render(request, 'administration/class_notification.html', context)



def contact(request):
    return render(request, 'administration/contact.html')


def facilities(request):
    return render(request, 'administration/facilities.html')


def notice(request):
    notices = Notice.objects.all()
    return render(request, 'administration/notice.html', context={'notices':notices})

@login_required
@student_required
def student_form(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(user = request.user.id)
        form = StudentForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('/student_profile')
        else:
            pi = Student.objects.get(user = request.user.id)
            form = StudentForm(instance = pi)
    else:
        form = StudentForm() 
    return render(request, 'administration/student_form.html', {'form':form})



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
    student = Student.objects.get(user_id = request.user.id)
    return render(request, 'administration/result.html', {'student':student})



def registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        print(form)
        if form.is_valid():
            name = request.POST['name']
            dob = request.POST['dob']
            phone = request.POST['phone']
            address = request.POST['address']
            email = request.POST['email']
            grade = request.POST['grade']
            form.save()

            messages.success(request, 'Registration Data Posted Successfully!')
            
    return render(request, 'administration/registration.html', {'form': form, 'messages':messages})     


@login_required
@student_required
def student(request):
    student = get_object_or_404(Student, user = request.user.id)
    return render(request, 'administration/student_profile.html',{'student':student})

