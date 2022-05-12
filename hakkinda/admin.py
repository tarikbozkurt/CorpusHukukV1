from django.contrib import admin

# Register your models here.
from hakkinda.models import Hakkinda,firmaOzellikleri


class HakkindaAdmin(admin.ModelAdmin):
    list_display = ['id','hakkinda_title','hakkinda_text','hakkinda_created_date']

admin.site.register(Hakkinda, HakkindaAdmin)

class firmaOzellikAdmin(admin.ModelAdmin):
    list_display = ['id','firmaOzellik_title','firmaOzellik_text','firmaOzellik_adet','firmaOzellik_icon','firmaOzellik_created_date']

admin.site.register(firmaOzellikleri, firmaOzellikAdmin)
