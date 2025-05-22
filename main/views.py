from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Contact
from socket import gaierror
import ssl
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone', '')
            service = request.POST.get('service')
            message = request.POST.get('message')

            # Save to database
            contact_entry = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                service=service,
                message=message
            )

            messages.success(request, 'Thank you for contacting us! We have received your message.')
            return redirect('contact')
        except Exception as e:
            print(f"Contact form error: {str(e)}")
            messages.error(request, 'There was an error sending your message. Please try again later.')

    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def industrial_gases(request):
    return render(request, 'services/industrial_gases.html')

def medical_gases(request):
    return render(request, 'services/medical_gases.html')

def cryogenic_equipment(request):
    return render(request, 'services/cryogenic_equipment.html')

def gas_cylinders(request):
    return render(request, 'services/gas_cylinders.html')

def gas_installations(request):
    return render(request, 'services/gas_installations.html')

def technical_services(request):
    return render(request, 'services/technical_services.html')