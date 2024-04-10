from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ExpenditureGrant, GrantSummary, Receipts, AllGrants, Datatable, ReceiptsExpenditure, BudgetTrends, BudgetProfile
import settings

@plugin_pool.register_plugin
class ExpenditureGrantPlugin(CMSPluginBase):
    model = ExpenditureGrant
    name = _("Expenditure - Grant")
    render_template = "grant_exp.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ExpenditureGrantPlugin, self).render(context, instance, placeholder)
        headHierarchy = "Grant Number, Major Head, Sub Major Head, Minor Head, Sub Head, Sub Sub Head, Detail Head, Sub detail Head"
        tableColumns = "Head of Account,Budget Entity,Head Description in English"
        context.update({
        	"fiscalYear" : {
                    "be"  : "Budget %s-%s" % (settings.FISCAL_YEAR, (settings.FISCAL_YEAR+1)%1000),
                    "actuals" : "Actuals %s-%s"% (settings.FISCAL_YEAR-2, (settings.FISCAL_YEAR-1)%1000),
                    "bePrev" : "Budget %s-%s"% (settings.FISCAL_YEAR-1, (settings.FISCAL_YEAR)%1000),
                    "re" : "Revised %s-%s" %  (settings.FISCAL_YEAR-1, (settings.FISCAL_YEAR)%1000)
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
                "be"  : "BUDGET_%s_%s" % (settings.FISCAL_YEAR, (settings.FISCAL_YEAR+1)%1000),
                "bePrev" : "BUDGET_%s_%s"% (settings.FISCAL_YEAR-1, (settings.FISCAL_YEAR)%1000),
                }
        	})
        return context

@plugin_pool.register_plugin
class ReceiptsPlugin(CMSPluginBase):
    model = Receipts
    name = _("Receipts")
    render_template = "receipts.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ReceiptsPlugin, self).render(context, instance, placeholder)
        headHierarchy =  "MAJOR, Major Head, Sub Major Head, Minor Head, Sub Head, Sub Sub Head, Detail Head, Sub detail Head"
        tableColumns = "Head Of Account,Head Description in English"
        context.update({
        	"fiscalYear" : {
                "be"  : "Budget %s-%s" % (settings.FISCAL_YEAR, (settings.FISCAL_YEAR+1)%1000),
                "actuals" : "Actuals %s-%s"% (settings.FISCAL_YEAR-2, (settings.FISCAL_YEAR-1)%1000),
                "bePrev" : "Budget %s-%s"% (settings.FISCAL_YEAR-1, (settings.FISCAL_YEAR)%1000),
                "re" : "Revised %s-%s" %  (settings.FISCAL_YEAR-1, (settings.FISCAL_YEAR)%1000)
   
        		},
        		'headHierarchy' : headHierarchy,
        		'tableColumns' : tableColumns,
        	})

        return context

class SmallMultiplesExpPlugin(CMSPluginBase):
    model = AllGrants
    name = _("All - Grants")
    render_template = "all_grants.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(SmallMultiplesExpPlugin, self).render(context, instance, placeholder)
        tableColumns = "Grant"
        context.update({
        	"fiscalYear" : {
        		"budget" : "2018-19", 
				"budget_2017" : "2017-18",
				"budget_2016" : "2016-17"
        		},
        		'tableColumns' : tableColumns
        	})
        return context

@plugin_pool.register_plugin
class DataTablePlugin(CMSPluginBase):
    model = Datatable
    name = _("Datatable")
    render_template = "datatable.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(DataTablePlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ReceiptsExpenditurePlugin(CMSPluginBase):
    model = ReceiptsExpenditure
    name = _("Receipts - Expenditure")
    render_template = "receipt_exp.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ReceiptsExpenditurePlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class BudgetTrendsPlugin(CMSPluginBase):
    model = BudgetTrends
    name = _("Budget - Trends")
    render_template = "budget_trends.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(BudgetTrendsPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class BudgetProfilePlugin(CMSPluginBase):
    model = BudgetProfile
    name = _("Budget - Profile")
    render_template = "budget_profile.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(BudgetProfilePlugin, self).render(context, instance, placeholder)
        context.update({
            "fiscalYear" : {
                "be" :"Budget Estimates %s-%s" % (settings.FISCAL_YEAR, (settings.FISCAL_YEAR+1)), 
                "bePrev" : "Budget Estimates %s-%s"% (settings.FISCAL_YEAR-1, (settings.FISCAL_YEAR)),
                }
            })


        return context
