from django.urls import path
from . import views
from project import settings
from django.conf.urls.static import static

app_name='shop'

urlpatterns = [
    path('help', views.help, name='help'),
    path('item/<int:item_id>', views.detail, name='detail'),
    path('', views.index, name='index'),
]
