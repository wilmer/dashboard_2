# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ControlOperacional


class ControlOperacionalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nombre_operador': ('nombre_operador',)}
    list_display = ('nombre_operador', 'codigo_equipo', 'fecha', 'metros_perforados', 'horas_operacion', 'turno')
    search_fields = ['nombre_operador']


admin.site.register(ControlOperacional, ControlOperacionalAdmin)
