from cms import constants
from cms.constants import TEMPLATE_INHERITANCE_MAGIC
from cms import api
api.create_page(title="Hello World4",language='en',template=TEMPLATE_INHERITANCE_MAGIC,parent=None)
