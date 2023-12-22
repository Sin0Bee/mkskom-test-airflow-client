from django.contrib import admin
from .models import MetaDAG


class DAGAdmin(admin.ModelAdmin):
    fields = ['name', 'file_path', 'interval']


admin.site.register(MetaDAG, DAGAdmin)
