from django.urls import path
from django_101.Tasks import views

urlpatterns = [
    path('', views.index),
    path('info/', views.all_the_information)
]
