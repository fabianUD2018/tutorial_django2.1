from django.urls import path 
from .views import home, about
urlpatterns = [
    path ('', home, name="posts"),
    path('about/', about, name='about')
]