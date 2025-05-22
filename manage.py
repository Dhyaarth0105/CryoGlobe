#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryoglobe.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# To create a Django superuser, run this command in your terminal:
# python manage.py createsuperuser
#
# Follow the prompts to enter username, email, and password.

# Here are the full steps to set up Django admin for your models:

# 1. **Register your models in admin.py**  
#    - Open each app's `admin.py` file (e.g., `yourapp/admin.py`).
#    - Register your models like this:
#      ```python
#      from django.contrib import admin
#      from .models import YourModel
# 
#      admin.site.register(YourModel)
#      ```
# 
# 2. **Make migrations for your models**  
#    - In your terminal, run:
#      ```
#      python manage.py makemigrations
#      ```
# 
# 3. **Apply migrations to the database**  
#    - Run:
#      ```
#      python manage.py migrate
#      ```
# 
# 4. **Create a superuser (if not done already)**  
#    - Run:
#      ```
#      python manage.py createsuperuser
#      ```
#    - Follow the prompts for username, email, and password.
# 
# 5. **Start the development server**  
#    - Run:
#      ```
#      python manage.py runserver
#      ```
# 
# 6. **Access the admin site**  
#    - Go to `http://127.0.0.1:8000/admin/` in your browser and log in with your superuser credentials.
