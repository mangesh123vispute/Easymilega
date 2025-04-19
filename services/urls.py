from django.urls import path
from .views import ServiceListView, ServiceProviderListView, ServiceProviderDetailView

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<str:service_name>/', ServiceProviderListView.as_view(), name='service-provider-list'),
    path('services/<str:service_name>/<int:service_provider_id>/', ServiceProviderDetailView.as_view(), name='service-provider-detail'),
]
