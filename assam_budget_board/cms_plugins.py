from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ExpenditureGrant, BalanceColumn, BarPlot

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
class BalanceColumnPlugin(CMSPluginBase):
    model = BalanceColumn
    name = _("Balance Column")
    render_template = "balance_column.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(BalanceColumnPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class BarPlotPlugin(CMSPluginBase):
    model = BarPlot
    name = _("Bar Plot")
    render_template = "barplot.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(BarPlotPlugin, self).render(context, instance, placeholder)
        return context