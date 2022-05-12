from django.contrib import admin

# Register your models here.
from base.models import PageSettings


class PageSettingsAdmin(admin.ModelAdmin):
    list_display = ['id','page_tag','page_title']

admin.site.register(PageSettings, PageSettingsAdmin)