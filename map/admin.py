# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import GeoPoint
from leaflet.admin import LeafletGeoAdmin
# Register your models here.



admin.site.register(GeoPoint, LeafletGeoAdmin)
