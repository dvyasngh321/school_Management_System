from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.views.generic import DetailView
from administration.decorators import principal_required, teachers_required
from .models import (Notice, Student, User, Result, MyClassTeacher, Event, 
                          Post, Comment,Gallery, TeacherLeaveApplication, ApplyForExamination, PublishResult)
from .decorators import student_required
from .forms import (RegistrationForm, StudentForm, StudentLeaveApplicationForm,
                     ContactForm, PostForm, CommentForm, ApplyForExaminationForm,TeacherLeaveApplicationForm)
from account.models import Account, TeacherAccount, Expense, Payment
from teacher.models import Message, Grade
from account.forms import ResultForm

# Create your views here.
def home_page(request):
    grade = Grade.objects.all()
    notices = Notice.objects.all().order_by('-created_date')[:15]
    event = Event.objects.all().order_by('-created_date').first()
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/success/')     
        else:
            form = ContactForm()
    return render(request, 'administration/home.html', {'grade':grade, 'notices':notices, 'event':event, 'form':form})

@login_required
def class_notification(request, class_id):
    grade = Grade.objects.all()
    if class_id:
        g = get_object_or_404(Grade, grade=class_id)
        notification = Message.objects.filter(grade = g).order_by('-created_date')[0:1]
    context ={'g':g, 'notification' : notification, 'grade':grade}    
    return render(request, 'administration/class_notification.html', context)

@login_required
def post(request):
    if request.method == 'POST':
        id = User.objects.get(username = request.user.username)
        form = PostForm(request.POST, instance = id)
        if form.is_valid():
            form = PostForm(request.POST, request.FILES)
            form.save() 
    else:
        id = User.objects.get(username = request.user.username)
        form = PostForm(instance = id)
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'administration/post.html', {'form':form, 'posts':posts})

@login_required
def mypost(request):
    posts = Post.objects.filter(author = request.user.id).order_by('-created_date')
    return render(request, 'administration/mypost.html', {'posts':posts})


@login_required
@student_required
def view_your_payment_history(request):
    try:
        account = Account.objects.get(user = request.user.id)
    except Account.DoesNotExist:
        account = None    
    payment = Payment.objects.filter(account = account).order_by('-created_date')
    return render(request, 'administration/payment_history.html', {'account':account, 'payment':payment})

@login_required
@student_required
def your_invoice(request):
    try:
        account = Account.objects.get(user = request.user.id)
    except Account.DoesNotExist:
        account = None    
    return render(request, 'administration/your_invoice.html', {'a':account})


@principal_required
def principal_profile(request):
    student = Student.objects.all()
    staff = TeacherAccount.objects.all()
    income = Payment.objects.all().values_list('paid', flat=True)
    total = sum(income)
    expense = Expense.objects.all().values_list('amount', flat=True)
    total_expense = sum(expense)
    context = {'student': student, 'staff':staff, 'total':total, 'total_expense':total_expense}
    return render(request, 'administration/principal.html', context)


@login_required
@principal_required
def view_teacher_leave_notification(request):
    applications = TeacherLeaveApplication.objects.all().order_by('-created_date')
    return render(request, 'administration/teacher_leave_notification.html',{'applications':applications})

@login_required
def post_delete(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(id = id)
        pi.delete()
        return redirect('/post/')

@login_required
def post_detail(request, id):
    if id:
        post = Post.objects.get(id = id)
        cmnts = Comment.objects.filter(post = post).order_by('-created_date')
        form = CommentForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                description = request.POST.get('description')
                comment = Comment.objects.create(post=post, author=request.user, description=description)
                comment.save()
            else:
                form = CommentForm()
    return render(request, "administration/post_detail.html", {'post':post, 'form':form, 'comment':cmnts})


def computer(request):
    return render(request, 'administration/computer.html')

def facilities(request):
    return render(request, 'administration/facilities.html')

                

def notice(request):
    notices = Notice.objects.all().order_by('-created_date')
    return render(request, 'administration/notice.html', context={'notices':notices})

@login_required
def event_detail(request, id):
    if id:
        event = Event.objects.get(id=id)
    return render(request, 'administration/event_detail.html', {'event':event})


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
    try:
        account = Account.objects.get(user = request.user.id)
    except Account.DoesNotExist:
        account = None    
    payment = Payment.objects.filter(account = account).order_by('-created_date').first()
    return render(request, 'administration/student_info.html', {'student':student, 'account':account, 'payment':payment})

@login_required
@student_required
def apply_for_examination(request):
    student = Student.objects.get(user = request.user.id)
    exam = PublishResult.objects.all().last()
    form = ApplyForExaminationForm(request.POST or None)
    if request.method == 'POST':
        name = request.POST.get("name")
        total = request.POST.get("total")
        remaining = request.POST.get("remaining_due")
        print(name, total, remaining)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        else:
            form = ApplyForExaminationForm()    
    return render(request, 'administration/apply_for_examination.html',{'student':student, 'form':form, 'exam':exam})    

@principal_required
def approve_application(request, id):
    if request.method == 'POST':
        pi = TeacherLeaveApplication.objects.get(pk = id)
        form = TeacherLeaveApplicationForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        pi = TeacherLeaveApplication.objects.get(pk=id)
        form = TeacherLeaveApplicationForm(instance = pi)
    return render(request, 'administration/approve_application.html', {'form':form})


def view_admit_card(request):
    student = Student.objects.get(user = request.user.id)
    try:
        card = ApplyForExamination.objects.get(name = request.user.username)
    except ApplyForExamination.DoesNotExist:
        card = None    
    return render(request, 'administration/admit_card.html', {'student':student, 'card':card})    

@login_required
def approved_application(request):
    application = TeacherLeaveApplication.objects.filter(user = request.user.username)
    return render(request, 'administration/approved_application.html', {'application':application})

@principal_required
def delete_app(request, id):
    if request.method == 'POST':
        pi = TeacherLeaveApplication.objects.get(pk =id)
        pi.delete()
        return redirect('/teacher_leave_application/')


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


def gallery(request):
    gallery = Gallery.objects.all().order_by('-created_date')
    return render(request, 'administration/gallery.html', {'gallery':gallery})


@login_required
@student_required
def result(request):
    student = Student.objects.get(user = request.user.id)
    try:
        result = Result.objects.get(username = request.user.username)
    except Result.DoesNotExist:
        result = None   
    published_result = PublishResult.objects.all().last()
    return render(request, 'administration/result.html', {'result':result, 'student':student,'published_result':published_result})



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
    return render(request,"administration/success.html")

@teachers_required
def teacher_leave_form(request):
    form = TeacherLeaveApplicationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/success/')
    return render(request, 'administration/teacher_leave_form.html', {'form':form})