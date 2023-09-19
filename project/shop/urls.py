from django.urls import path
from . import views
from project import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('item/<int:item_id>', views.detail, name='detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)