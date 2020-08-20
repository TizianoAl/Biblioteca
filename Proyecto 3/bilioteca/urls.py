from django.urls import path, include
from bilioteca.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
