from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Service, ServiceProvider, CustomerRequest
from .serializers import ServiceSerializer, ServiceProviderSerializer, CustomerRequestSerializer

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

class CustomerRequestCreateView(generics.CreateAPIView):
    serializer_class = CustomerRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer_request = serializer.save()
            
            # Prepare email context
            context = {
                'name': customer_request.name,
                'service': customer_request.service.name,
                'time_slot': customer_request.preferred_time_slot,
                'address': customer_request.address,
                'mobile': customer_request.mobile_number,
                'status': 'Unresolved',
                'created_at': customer_request.timestamp.strftime('%B %d, %Y at %I:%M %p')
            }
            
            # Render HTML email template
            html_message = render_to_string('services/emails/new_request.html', context)
            
            try:
                # Create email message
                email = EmailMessage(
                    subject='New Service Request',
                    body=html_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.ADMIN_EMAIL],
                )
                email.content_subtype = 'html'  # Set content type to HTML
                email.send(fail_silently=False)
            except Exception as e:
                # Log the error but don't fail the request
                print(f"Failed to send email: {str(e)}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)