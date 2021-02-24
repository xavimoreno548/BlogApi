from django.contrib import admin
from apps.core.models import Language


# Register your models
class LanguageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Language, LanguageAdmin)
