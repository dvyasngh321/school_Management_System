from django.contrib import admin
from .models import Invoices, Account, TeacherAccount

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name', 'grade']


admin.site.register(Account)
admin.site.register(Invoices)
admin.site.register(TeacherAccount)