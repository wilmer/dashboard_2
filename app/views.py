# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Country
from .serializers import CountrySerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root
    :param request:
    :param format:
    :return: Response
    """
    return Response({
        # 'countries': reverse('countries', request=request, format=format),
    })


def country_population(request):
    context = {}
    return render(request, 'app/country_population.html', context)


class CountryViewSet(viewsets.ModelViewSet):
    """
    List all Delivered Orders for logged in user.
    """
    serializer_class = CountrySerializer

    def get_queryset(self):
        queryset = Country.objects.all()
        return queryset
