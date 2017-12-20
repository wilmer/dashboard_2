# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    iso_codes = models.CharField(max_length=10)
    population = models.IntegerField()
    area = models.IntegerField()
    gdp = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name
