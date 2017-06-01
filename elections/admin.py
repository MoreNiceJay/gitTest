# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Candidate, Poll, Choice
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Choice)

