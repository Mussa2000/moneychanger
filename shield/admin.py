from django.contrib import admin

from shield.models.alert import Alert
from shield.models.document import Document
from shield.models.folder import Folder

# Register your models here.
admin.site.register(Document)
admin.site.register(Alert)
admin.site.register(Folder)