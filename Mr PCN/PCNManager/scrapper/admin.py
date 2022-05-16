from django.contrib import admin
from .models import PCN

# custom pcn 
class PCNAdmin(admin.ModelAdmin):
    list_display = ('pcn', 'owner', 'location', 'subdivision', 'legal_description', 'control_number')
    list_filter = ('pcn', 'owner', 'location', 'subdivision', 'legal_description', 'control_number')
    search_fields = ('pcn', 'owner', 'location', 'subdivision', 'legal_description', 'control_number')

admin.site.register(PCN, PCNAdmin)
