from django.contrib import admin
from .models import Csv, csv_client

# Register your models here.
admin.site.register(Csv)
admin.site.register(csv_client)