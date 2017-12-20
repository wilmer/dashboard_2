# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'country_name': ('country_name',)}
    list_display = ('country_name', 'country_code', 'iso_codes', 'population', 'area', 'gdp')
    search_fields = ['country_name']

admin.site.register(Country, CountryAdmin)

