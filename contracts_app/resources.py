from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Contract


class ContractResource(resources.ModelResource):

    class Meta:
        model = Contract
