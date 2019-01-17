from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import ExpenditureGrant, AllGrants, BalanceColumn


@plugin_pool.register_plugin
class ExpenditureGrantPlugin(CMSPluginBase):
    model = ExpenditureGrant
    name = _("Expenditure - Grant")
    render_template = "grant_exp.html"
    cache = True

   
    def render(self, context, instance, placeholder):
        context = super(ExpenditureGrantPlugin, self).render(context, instance, placeholder)
        headHierarchy = "Grant Number, Major Head, Sub Major Head, Minor Head, Sub Head, Sub Sub Head, Detail Head, Sub detail Head"
        tableColumns = "Head Of Account,Budget Entity,Head Description,Head Description Assamese"
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
class BalanceColumnPlugin(CMSPluginBase):
    model = BalanceColumn
    name = _("Balance Column")
    render_template = "balance_column.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(BalanceColumnPlugin, self).render(context, instance, placeholder)
        return context
