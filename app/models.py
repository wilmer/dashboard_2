# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ControlOperacional(models.Model):
    nombre_operador = models.CharField(max_length=100)
    codigo_equipo = models.CharField(max_length=10)
    fecha = models.CharField(max_length=10)
    metros_perforados = models.IntegerField()
    horas_operacion = models.IntegerField()
    turno = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_operador
