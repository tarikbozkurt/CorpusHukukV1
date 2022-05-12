from django.contrib import admin

# Register your models here.
from iletisim.models import firmaBilgi


class firmaBilgiAdmin(admin.ModelAdmin):
    list_display = ['id','firma_adi','firma_kurulus_tarihi','firma_email','firma_telefon']

admin.site.register(firmaBilgi,firmaBilgiAdmin)
