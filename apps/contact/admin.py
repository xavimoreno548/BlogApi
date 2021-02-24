from django.contrib import admin
from apps.contact.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'email', 'message', 'created', 'updated']


admin.site.register(Contact, ContactAdmin)