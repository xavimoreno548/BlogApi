from django.urls import path
from apps.home.views.home_text_view import HomeTextView

urlpatterns = [
    path('', HomeTextView.as_view())
]
