from django.contrib import admin
from .models import Account, TeacherAccount, Expense, Payment

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name', 'grade']


admin.site.register(Account)
admin.site.register(TeacherAccount)
admin.site.register(Expense)
admin.site.register(Payment)