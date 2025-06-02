from django.contrib import admin
from .models import Contact
from .models import AboutPageImage
from .models import ServicePageImage

admin.site.register(Contact)
admin.site.register(AboutPageImage)
admin.site.register(ServicePageImage)

# Register your models here.
