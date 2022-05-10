
from django.urls import path
from django.conf.urls import url
from test1 import views

urlpatterns = [
    path('index/', views.index),
]