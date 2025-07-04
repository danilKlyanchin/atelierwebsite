from django.urls import path
from . import views

urlpatterns = [
    path('', views.entities_list, name='entities_list'),
]
