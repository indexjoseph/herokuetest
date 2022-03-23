from django.contrib import admin
from code_journals.models import Entry, Topic
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)