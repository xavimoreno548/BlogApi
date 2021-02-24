from django.urls import path
from apps.home.views.home_text import HomeTextView

urlpatterns = [
    path('', HomeTextView.as_view())
]
