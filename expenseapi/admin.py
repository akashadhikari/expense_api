from django.contrib import admin

# Register your models here.
from .models import Company, Billing

admin.site.register(Company)
admin.site.register(Billing)