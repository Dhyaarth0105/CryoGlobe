from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('services/industrial-gases/', views.industrial_gases, name='industrial_gases'),
    path('services/medical-gases/', views.medical_gases, name='medical_gases'),
    path('services/cryogenic-equipment/', views.cryogenic_equipment, name='cryogenic_equipment'),
    path('services/gas-cylinders/', views.gas_cylinders, name='gas_cylinders'),
    path('services/gas-installations/', views.gas_installations, name='gas_installations'),
    path('services/technical-services/', views.technical_services, name='technical_services'),
]

