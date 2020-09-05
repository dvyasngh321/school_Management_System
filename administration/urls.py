from django.urls import path
from . import views
from .views import NoticeDetailView

urlpatterns = [
    path('',views.home_page, name="home"),
    path('notice/', views.notice, name="notice"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('facilities/', views.facilities, name="facilities"),
    path('computer/', views.computer, name="computer"),
    path('library/', views.library, name="library"),
    path('laboratory/', views.laboratory, name="laboratory"),
    path('sports/', views.sports, name="sports"),
    path('result/', views.result, name="result"),
    path('student_info/', views.student_info, name="student_info"),
    path('apply_for_registration/', views.registration, name="apply_for_registration"),
    path('apply_for_leave/', views.student_leave_form, name="apply_for_leave"),
    path('login/', views.login, name="login"),
    path('success/', views.success, name="success"),
    path('profile/', views.student, name="student_profile"),
    path('logout/', views.logout, name="logout"),
    path('student_form/<id>/', views.student_form, name="student_form"),
    path('class/<class_id>/', views.class_notification, name="class_notification"),
    path('notice/<pk>/', views.NoticeDetailView.as_view(), name="notice-detail"),
]