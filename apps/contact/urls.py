from django.urls import path
from apps.contact.views.contact import ContactView

urlpatterns = [
    path('', ContactView.as_view())
]