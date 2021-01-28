from django.contrib import admin
from .models import employees
# Register your models here.
#admin.site.register(employees)
@admin.register(employees)
class employeesAdmin(admin.ModelAdmin):
    list_display =['id', 'first_name', 'last_name', 'email', 'phone']