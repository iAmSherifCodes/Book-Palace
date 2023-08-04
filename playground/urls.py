from . import views
from django.urls import path

urlpatterns = [
    path('welcome/', views.welcome),
    path('hello/', views.hello)
]
