from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ExpenditureGrant, Receipts

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
class ReceiptsPlugin(CMSPluginBase):
    model = Receipts
    name = _("Receipts")
    render_template = "receipts.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ReceiptsPlugin, self).render(context, instance, placeholder)
        headHierarchy =  "MAJOR, Major Head, Sub-Major Head, Minor Head, Sub-Minor Head, Detailed Head, Object Head, Voucher Head"
        tableColumns = "HEAD OF ACCOUNT,HEAD DESCRIPTION"
        context.update({
        	"fiscalYear" : {
        		"be" : "BUDGET 2018-19", 
        		"actuals" : "ACTUALS 2016-17",
				"bePrev" : "BUDGET 2017-18",
				"re" : "REVISED 2017-18"
        		},
        		'headHierarchy' : headHierarchy,
        		'tableColumns' : tableColumns,
        	})

        return context