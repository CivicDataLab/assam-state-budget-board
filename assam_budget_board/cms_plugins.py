from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import *

@plugin_pool.register_plugin
class ExpenditureGrantPlugin(CMSPluginBase):
    model = ExpenditureGrant
    name = _("Expenditure - Grant")
    render_template = "grant_exp.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ExpenditureGrantPlugin, self).render(context, instance, placeholder)
        context.update({
        	"fiscal_year" : {
        		"be" : "2018-19 Budget Estimates", 
        		"actuals" : "2016-17 Actuals",
				"be_prev" : "2017-18 Budget Estimates",
				"re" : "2017-18 Revised Estimates"
        		}
        	})
        return context

@plugin_pool.register_plugin
class SmallMultiplesExpPlugin(CMSPluginBase):
    model = SmallMultipleExpenditure
    name = _("Expenditure - SmallMultiples")
    render_template = "smallmultiples_exp.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(SmallMultiplesExpPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class DataTableExpPlugin(CMSPluginBase):
    model = DataTableExpenditure
    name = _("Expenditure - Grant")
    render_template = "grant_exp.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(DataTableExpPlugin, self).render(context, instance, placeholder)
        context.update({
        	"fiscal_year" : {
        		"be" : "2018-19 Budget Estimates", 
        		"actuals" : "2016-17 Actuals",
				"be_prev" : "2017-18 Budget Estimates",
				"re" : "2017-18 Revised Estimates"
        		}
        	})
        return context
