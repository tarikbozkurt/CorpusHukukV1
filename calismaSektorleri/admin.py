from django.contrib import admin

# Register your models here.
from calismaSektorleri.models import Sektorler


class SektorlerAdmin(admin.ModelAdmin):
    list_display = ['id','sektor_adi']

admin.site.register(Sektorler,SektorlerAdmin)
