from cms import api
from cms.models import Page
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

def run():
    page = api.create_page(title="Sub-grant",language='en',template='content_1.html',parent= Page.objects.get(pk=1))
    placeholder = page.placeholders.get(slot='grant placeholder')
    
    api.add_plugin(placeholder,'ExpenditureGrantPlugin', language = 'en', position = 'first-sibling', **{'url': 'https://openbudgetsindia.org/dataset/69b68cf0-d032-4cf2-a842-72f9936c7009/resource/932d3e42-cfaf-4602-8fdc-91d25bd2fd64/download/24---aid-materials.csv'})
