from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.code
