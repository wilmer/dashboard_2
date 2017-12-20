# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def country_population(request):
	context = {}
	return render(request, 'app/country_population.html', context)
