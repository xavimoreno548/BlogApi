from django.db import models
from apps.core.models import Language


# Create your models here.
class HomeText(models.Model):
    title = models.CharField(max_length=190)
    main_text = models.TextField()
    secondary_text = models.TextField()
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title
