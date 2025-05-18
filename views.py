from django.shortcuts import render

def home(request):
    pass

def about(request):
    pass

def contact(request):
    pass

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    pass

def services(request):
    return render(request, 'services.html')
