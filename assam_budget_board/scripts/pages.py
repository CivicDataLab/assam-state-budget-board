from cms import api
from cms.models import Page
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

title = open('assam_budget_board/static/resource_titles.txt', "r")
urls = open('assam_budget_board/static/resource_urls.txt', "r")
url = []
titles = []
for x in urls:
   url.append(x.strip('\n'))

for y in title:
   titles.append(y.strip('\n'))
  
def run():
    for i in range(0,len(url)):
       page = api.create_page(title= titles[i],language='en',template='content_1.html',parent= Page.objects.get(pk=182))
       placeholder = page.placeholders.get(slot='grant placeholder')
       api.add_plugin(placeholder,'ExpenditureGrantPlugin', language = 'en', position = 'first-sibling', **{'url': url[i]})
  


