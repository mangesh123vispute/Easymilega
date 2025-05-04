from django.db import models

class Service(models.Model):
    name = models.TextField()  
    icon_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    profile_pic = models.TextField(blank=True, null=True)   
    name = models.TextField() 
    description = models.TextField(blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='providers')
    rating = models.FloatField(default=0.0, blank=True, null=True)
    availability = models.BooleanField(default=True)
    experience = models.FloatField(default=0.0, help_text="Experience in years", blank=True, null=True)

    @property
    def global_number(self):
        global_settings = GlobalSettings.objects.first()
        return global_settings.service_provider_number if global_settings else 100  

    def __str__(self):
        return self.name

class GlobalSettings(models.Model):
    service_provider_number = models.BigIntegerField(default=100000000000)  

    def __str__(self):
        return f"Service Provider Number: {self.service_provider_number}"

class CustomerRequest(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    service = models.TextField()
    address = models.TextField()
    preferred_time_slot = models.CharField(max_length=50)
    delivery_date = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Request by {self.name} for {self.service}"

