# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from decimal import Decimal

# Create your models here.
class MoodmetricLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    time = models.DateTimeField(null=False, blank=False)
    mmnumber = models.DecimalField(max_digits=4,decimal_places=2,default=Decimal('0.00'))
    scv = models.DecimalField(max_digits=4,decimal_places=2,default=Decimal('0.00'))
    scr_freq = models.IntegerField()
    scl = models.DecimalField(max_digits=5,decimal_places=3,default=Decimal('0.00'))
    step_count = models.IntegerField()
    raw_mm = models.IntegerField()

    def __unicode__(self):
        return self.name