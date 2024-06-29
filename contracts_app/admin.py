from django.contrib import admin
from .models import Contract, Attachment
from .resources import ContractResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 0
    fields = ['creator', 'file']


class ContractAdmin(ImportExportModelAdmin):
    inlines = [AttachmentInline]
    resource_class = ContractResource


admin.site.register(Contract, ContractAdmin)
