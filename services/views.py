from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Service, ServiceProvider
from .serializers import ServiceSerializer, ServiceProviderSerializer

# 1. /services - Get all services
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# 2. /services/<service_name>/ - Get service providers by service name
class ServiceProviderListView(generics.ListAPIView):
    serializer_class = ServiceProviderSerializer

    def get_queryset(self):
        service_name = self.kwargs.get('service_name')
        try:
            # Case-insensitive search for service name
            service = Service.objects.get(name__iexact=service_name)
            return ServiceProvider.objects.filter(service=service)
        except Service.DoesNotExist:
            return ServiceProvider.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": f"No service providers found for service: {self.kwargs.get('service_name')}"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 3. /services/<service_name>/<provider_id>/ - Get details of a specific service provider
class ServiceProviderDetailView(generics.RetrieveAPIView):
    serializer_class = ServiceProviderSerializer

    def get_object(self):
        service_name = self.kwargs.get("service_name")
        provider_id = self.kwargs.get("service_provider_id")
        
        # Get the service by name (case-insensitive)
        service = get_object_or_404(Service, name__iexact=service_name)
        
        # Get the service provider
        return get_object_or_404(
            ServiceProvider,
            id=provider_id,
            service=service
        )