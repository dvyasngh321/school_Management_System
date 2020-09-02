from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_account, name='account'),
    path('add_student/', views.account_page, name='account_page'),
    path('teacher_account_form/', views.teacher_account_form, name='teacher_account_form'),
    path('teacher_account_detail/', views.teacher_account_detail, name='teacher_account_detail'),
    path('information/', views.account_information, name='information'),
    path('update/<int:id>/', views.update_information, name='update_information'),
    path('update_teacher_data/<int:id>/', views.update_teacher_data, name='update_teacher_data'),
    path('delete/<int:id>/', views.delete_information, name="delete_information"),
    path('delete_teacher_data/<int:id>/', views.delete_teacher_data, name="delete_teacher_data"),
    path('invoice/<int:id>/', views.invoice, name="invoice"),
]