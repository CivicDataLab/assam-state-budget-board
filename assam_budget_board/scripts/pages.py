from cms import api
from cms.models import Page
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


urls = open('/home/ubuntu/Downloads/obi_links.txt', "r")
title = open('/home/ubuntu/Downloads/page_titles.txt', "r")
url = []
titles = []
for x in urls:
   url.append(x.strip('\n'))
for y in title:
   titles.append(y.strip('\n'))
  
def run():
    for i in range(0,81):
       page = api.create_page(title= titles[i],language='en',template='content_1.html',parent= Page.objects.get(pk=324))
       placeholder = page.placeholders.get(slot='grant placeholder')
  
       api.add_plugin(placeholder,'ExpenditureGrantPlugin', language = 'en', position = 'first-sibling', **{'url': url[i]})


