from django.contrib import admin

# Register your models here.
from vlog.models import Vlog


class VlogAdmin(admin.ModelAdmin):
    list_display = ['id','post_title','post_text','post_created_date']

admin.site.register(Vlog, VlogAdmin)
