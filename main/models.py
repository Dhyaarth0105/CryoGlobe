from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class AboutPageImage(models.Model):
    image = models.ImageField(upload_to='about/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"About Page Image ({self.id})"


class ServicePageImage(models.Model):
    PAGE_CHOICES = [
        ('industrial_gases', 'Industrial Gases'),
        ('medical_gases', 'Medical Gases'),
        ('cryogenic_equipment', 'Cryogenic Equipment'),
        ('gas_cylinders', 'Gas Cylinders'),
        ('gas_installations', 'Gas Installations'),
        ('technical_services', 'Technical Services'),
    ]
    page = models.CharField(max_length=32, choices=PAGE_CHOICES, unique=True)
    image = models.ImageField(upload_to='services/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_page_display()} Image"
