from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Service, ServiceProvider, GlobalSettings

class ServiceProviderResource(resources.ModelResource):
    service = fields.Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, field='id') 
    )

    class Meta:
        model = ServiceProvider
        fields = ('id', 'name', 'description', 'service', 'rating', 'availability', 'experience')

@admin.register(ServiceProvider)
class ServiceProviderAdmin(ImportExportModelAdmin):
    resource_class = ServiceProviderResource
    list_display = ('id','name', 'service', 'rating', 'availability', 'experience')
    search_fields = ('name', 'service__id')
    list_filter = ('availability', 'service')

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        fields = ('id', 'name', 'icon_link')

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    list_display = ('id', 'name', 'icon_link')
    search_fields = ('name',)

@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ('id','service_provider_number',)
