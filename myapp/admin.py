from django.contrib import admin

# Register your models here.
from myapp.models import Student, Customer


@admin.register(Student)
class Student_admin_register(admin.ModelAdmin):
    list_display = ['name']
    pass

@admin.register(Customer)
class Customer_admin_register(admin.ModelAdmin):
    list_display = ['first_name']
    pass