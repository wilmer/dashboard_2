# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ControlOperacional
from .serializers import ControlOperacionalSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root
    :param request:
    :param format:
    :return: Response
    """
    return Response({
        # 'controloperacional': reverse('countries', request=request, format=format),
    })


def metros_perforados(request):
    context = {}
    return render(request, 'app/chart.html', context)


class ControlOperacionalViewSet(viewsets.ModelViewSet):
    """
    List all Countries
    """
    serializer_class = ControlOperacionalSerializer

    def get_queryset(self):
        queryset = ControlOperacional.objects.all()
        return queryset
