from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]

# If this file is your app's urls.py, you do NOT need to add include() here.
# But in your PROJECT's urls.py (usually d:\Dhyaarth_Technology\Clients\CryoGlobeEnergy.com\Source_code\cryoglobe\cryoglobe\urls.py),
# you MUST include your app's urls like this:

# from django.urls import path, include
# urlpatterns = [
#     path('', include('cryoglobe.urls')),  # or 'main.urls' if your app is named 'main'
# ]