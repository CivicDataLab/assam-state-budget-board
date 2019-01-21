from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ExpenditureGrant, GrantSummary

@plugin_pool.register_plugin
class ExpenditureGrantPlugin(CMSPluginBase):
    model = ExpenditureGrant
    name = _("Expenditure - Grant")
    render_template = "grant_exp.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ExpenditureGrantPlugin, self).render(context, instance, placeholder)
        headHierarchy = "GRANT NUMBER, Major Head, Sub Major Head, Minor Head, Sub Head, Sub Sub Head, Detail Head, Sub detail Head"
        tableColumns = "HEAD OF ACCOUNT,BUDGET ENTITY,HEAD DESCRIPTION,HEAD DESCRIPTION ASSAMESE"
        context.update({
        	"fiscalYear" : {
        		"be" : "2018-19 Budget Estimates", 
        		"actuals" : "2016-17 Actuals",
				"bePrev" : "2017-18 Budget Estimates",
				"re" : "2017-18 Revised Estimates"
        		},
        		'headHierarchy' : headHierarchy,
        		'tableColumns' : tableColumns,
        	})

        return context

@plugin_pool.register_plugin
class GrantSummaryPlugin(CMSPluginBase):
    model = GrantSummary
    name = _("Grant - Summary")
    render_template = "grant_summary.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(GrantSummaryPlugin, self).render(context, instance, placeholder)
        context.update({
        	"fiscalYear" : {
        		"be" : "Budget 2018-19", 
        		"actuals" : "Actuals 2016-17",
				"bePrev" : "Budget 2017-18",
				"re" : "Revised 2017-18"
        		}
        	})

        return context