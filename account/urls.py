from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_account, name='account'),
    path('add_student/', views.account_page, name='account_page'),
    path('teacher_account_form/', views.teacher_account_form, name='teacher_account_form'),
    path('teacher_account_detail/', views.teacher_account_detail, name='teacher_account_detail'),
    path('information/', views.account_information, name='information'),
    path('expense/', views.expense, name='expense'),
    path('search/', views.search, name='search'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('approve_form/', views.approve_student_for_exam, name="approve_form"),
    path('update/<int:id>/', views.update_information, name='update_information'),
    path('confirm/<id>/', views.confirm_approval, name='confirm_approval'),
    path('payment/<id>/', views.payment, name='payment'),
    path('update_teacher_data/<int:id>/', views.update_teacher_data, name='update_teacher_data'),
    path('delete/<int:id>/', views.delete_information, name="delete_information"),
    path('delete_teacher_data/<int:id>/', views.delete_teacher_data, name="delete_teacher_data"),
    path('invoice/<int:id>/', views.invoice, name="invoice"),
    path('view_payment/<int:id>/', views.view_Payment, name="view_payment"),
    path('paybill/<int:id>/', views.paybill, name="paybill"),
]