from cms.models.pluginmodel import CMSPlugin
from django.db import models

class ExpenditureGrant(CMSPlugin):
    url = models.URLField(max_length=300)