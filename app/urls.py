from django.conf.urls import url
from .views import *

controloperacionales = ControlOperacionalViewSet.as_view({'get': 'list'})

urlpatterns = [
    url(r'^$', metros_perforados, name='metros_perforados'),
    url(r'^api/v1/controloperacional/$', controloperacionales, name='controloperacionales'),
]
