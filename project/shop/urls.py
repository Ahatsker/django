from django.urls import path
from . import views
from project import settings

urlpatterns = [
    path('', views.index, name='index')
]