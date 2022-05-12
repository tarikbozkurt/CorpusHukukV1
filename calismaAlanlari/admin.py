from django.contrib import admin

# Register your models here.
from calismaAlanlari.models import CalismaAlanlari


class CalismaAlanarimizAdmin(admin.ModelAdmin):
    list_display = ['id','calisma_title','calisma_created_date']

admin.site.register(CalismaAlanlari, CalismaAlanarimizAdmin)
