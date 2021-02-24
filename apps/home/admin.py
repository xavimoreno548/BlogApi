from django.contrib import admin
from apps.home.models import HomeText


# Register your models here.
class HomeTextAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(HomeText, HomeTextAdmin)
