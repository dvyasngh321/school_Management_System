from django.urls import path
from . import views
from .views import NoticeDetailView

urlpatterns = [
    path('',views.home_page, name="home"),
    path('notice/', views.notice, name="notice"),
    path('facilities/', views.computer, name="computer"),
    path('result/', views.result, name="result"),
    path('student_info/', views.student_info, name="student_info"),
    path('apply_for_registration/', views.registration, name="apply_for_registration"),
    path('apply_for_leave/', views.student_leave_form, name="apply_for_leave"),
    path('login/', views.login, name="login"),
    path('payment_history/', views.view_your_payment_history, name="payment_history"),
    path('gallery/', views.gallery, name="gallery"),
    path('your_invoice/', views.your_invoice, name="your_invoice"),
    path('admit_card/', views.view_admit_card, name="admit_card"),
    path('principal_profile/', views.principal_profile, name="principal"),
    path('post/', views.post, name="post"),
    path('success/', views.success, name="success"),
    path('apply_for_examination/', views.apply_for_examination, name="apply_for_examination"),
    path('profile/', views.student, name="student_profile"),
    path('mypost/', views.mypost, name="mypost"),
    path('logout/', views.logout, name="logout"),
    path('teacher_leave_form/', views.teacher_leave_form, name="teacher_leave_form"),
    path('approved_application/', views.approved_application, name="approved_application"),
    path('teacher_leave_application/', views.view_teacher_leave_notification, name="teacher_leave_application"),
    path('student_form/<id>/', views.student_form, name="student_form"),
    path('delete_app/<id>/', views.delete_app, name="delete_app"),
    path('approve/<id>/', views.approve_application, name="approve_application"),
    path('class/<class_id>/', views.class_notification, name="class_notification"),
    path('event_detail/<id>', views.event_detail, name="event_detail"),
    path('post_detail/<id>', views.post_detail, name="post_detail"),
    path('post_delete/<id>', views.post_delete, name="post_delete"),
    path('notice/<pk>/', views.NoticeDetailView.as_view(), name="notice-detail"),
    
]