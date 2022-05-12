from django.contrib import admin

# Register your models here.
from employee.models import Employee, EmployeeInformations


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','user_name']

admin.site.register(Employee, EmployeeAdmin)

class EmployeeInformationsAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','unvan','user_email','user_phone','about_user','user_image']

admin.site.register(EmployeeInformations, EmployeeInformationsAdmin)



