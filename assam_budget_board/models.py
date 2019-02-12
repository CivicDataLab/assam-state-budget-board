from cms.models.pluginmodel import CMSPlugin
from django.db import models

class ExpenditureGrant(CMSPlugin):
    url = models.URLField(max_length=300)


class GrantSummary(CMSPlugin):
    url = models.URLField(max_length=300)


class Receipts(CMSPlugin):
    url = models.URLField(max_length=300)

class AllGrants(CMSPlugin):
    url = models.URLField(max_length=300)

class Datatable(CMSPlugin):
    url = models.URLField(max_length=300)
    columns = models.CharField(max_length=500, default='None')

class ReceiptsExpenditure(CMSPlugin):
    url = models.URLField(max_length=300)
   
class BudgetTrends(CMSPlugin):
    url = models.URLField(max_length=500)


