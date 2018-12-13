# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework import viewsets

from .serializers import GeoPointSerializer
from .models import GeoPoint


class GeoPointViewSet(viewsets.ModelViewSet):
    queryset = GeoPoint.objects.all()
    serializer_class = GeoPointSerializer
