from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    message = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null= True, blank=True)

    def __str__(self):
        return self.email
