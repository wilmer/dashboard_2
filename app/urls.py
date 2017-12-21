from django.conf.urls import url
from .views import *

countries = CountryViewSet.as_view({'get': 'list'})

urlpatterns = [
    url(r'^$', country_population, name='country-population'),
    url(r'^api/v1/country/$', countries, name='countries'),
]
