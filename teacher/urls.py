from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_page, name="teacher_page"),
    path('classteacher/', views.class_teacher_page, name="classteacher"),
    path('add_your_class/', views.add_your_class, name="classteacher_class"),
    path('add_class_notification/', views.add_class_notification, name="add_class_notification"),
    path('leave_notifications/', views.leave_notifications, name="leave_notifications"),
    path('manage_result/<class_id>', views.manage_result, name="manage_result"),
    path('delete_result/<id>', views.delete_result, name="delete_result"),
    path('update_result/<id>', views.update_result, name="update_result"),
    path('delete_leave_notification/<id>/', views.delete_leave_notification, name="delete_leave_notification"),
]