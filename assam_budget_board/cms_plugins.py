from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ExpenditureGrant, AllGrants

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
        		"budget" : "Budget 2018-19", 
				"budget_2017" : "Budget 2017-18",
				"budget_2016" : "Budget 2016-17"
        		},
        		'tableColumns' : tableColumns
        	})
        return context

