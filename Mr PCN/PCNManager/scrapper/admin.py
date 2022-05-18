from calendar import c
from django.contrib import admin
from .models import PCN, directory
import csv

def download_csv(modeladmin, request, queryset):
    f = open('some.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(["pcn", "owner", "email", "phone", "location", "legal_description", "control_number", "subdivision"])
    for s in queryset:
        writer.writerow([s.pcn, s.owner, s.email, s.phone, s.location, s.legal_description, s.control_number, s.subdivision])

# custom pcn 
class PCNAdmin(admin.ModelAdmin):
    list_display = ('pcn', 'owner', 'location', 'email', 'phone', 'subdivision', 'legal_description', 'control_number')
    list_filter = ('pcn', 'owner', 'location', 'subdivision', 'legal_description', 'control_number')
    search_fields = ('pcn', 'owner', 'location', 'subdivision', 'legal_description', 'control_number')
    # pagination
    actions = [download_csv]


class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone1', 'phone2', 'address', 'city', 'state', 'zip', 'community')
    list_filter = ('state',)
    search_fields = ('fname', 'lname', 'email', 'email_old', 'phone1', 'phone1_old', 'phone2', 'phone2_old', 'address', 'city', 'state', 'zip', 'community')

admin.site.register(PCN, PCNAdmin)
admin.site.register(directory, DirectoryAdmin)