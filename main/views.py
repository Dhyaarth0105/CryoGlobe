from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Contact, AboutPageImage, ServicePageImage
from socket import gaierror
import ssl
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def about(request):
    about_image = AboutPageImage.objects.last()
    return render(request, 'about.html', {'about_image': about_image})

def contact(request):
    form = {}
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        # Basic validation
        errors = {}
        if not name:
            errors['name'] = "Name is required."
        if not email:
            errors['email'] = "Email is required."
        if not service:
            errors['service'] = "Service is required."
        if not message:
            errors['message'] = "Message is required."

        form = {
            'name': name,
            'email': email,
            'phone': phone,
            'service': service,
            'message': message,
            'errors': errors
        }

        if errors:
            messages.error(request, 'There was an error sending your message. Please check the form and try again.')
            return render(request, 'contact.html', {'form': form})

        try:
            # Save to database
            contact_entry = Contact.objects.create(
                name=name,
                email=email,
                service=service,
                message=message
            )
            messages.success(request, 'Thank you for contacting us! We have received your message.')
            return redirect('contact')
        except Exception as e:
            import traceback
            print("Contact form error:", str(e))
            traceback.print_exc()  # This will print the full error stack trace
            messages.error(request, f'There was an error sending your message. Please try again later. ({str(e)})')
            return render(request, 'contact.html', {'form': form})

    return render(request, 'contact.html', {'form': form})

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def industrial_gases(request):
    image = ServicePageImage.objects.filter(page='industrial_gases').first()
    return render(request, 'services/industrial_gases.html', {'service_image': image})

def medical_gases(request):
    image = ServicePageImage.objects.filter(page='medical_gases').first()
    return render(request, 'services/medical_gases.html', {'service_image': image})

def cryogenic_equipment(request):
    image = ServicePageImage.objects.filter(page='cryogenic_equipment').first()
    return render(request, 'services/cryogenic_equipment.html', {'service_image': image})

def gas_cylinders(request):
    image = ServicePageImage.objects.filter(page='gas_cylinders').first()
    return render(request, 'services/gas_cylinders.html', {'service_image': image})

def gas_installations(request):
    image = ServicePageImage.objects.filter(page='gas_installations').first()
    return render(request, 'services/gas_installations.html', {'service_image': image})

def technical_services(request):
    image = ServicePageImage.objects.filter(page='technical_services').first()
    return render(request, 'services/technical_services.html', {'service_image': image})

