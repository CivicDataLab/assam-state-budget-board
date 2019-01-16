from cms.models.pluginmodel import CMSPlugin
from django.db import models

class ExpenditureGrant(CMSPlugin):
    url = models.URLField(max_length=300)

class BalanceColumn(CMSPlugin):
    url = models.URLField(max_length=300)


class BarPlot(CMSPlugin):
    url = models.URLField(max_length=300)
    column = models.CharField(max_length=50, default='None')
    field = models.CharField(max_length=200, default='None')