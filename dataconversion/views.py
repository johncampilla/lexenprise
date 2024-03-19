from django.http import HttpResponse
from django.shortcuts import render
from .models import Csv, csv_client


import csv


# Create your views here.
# def upload_file_view(request):

#     form = CsvForm(request.POST or None, request.FILES or None)

#     if form.is_valid():
#         form.save()
#         form = CsvForm()
#         obj = Csv.objects.get(activated = False)
#         print(obj)
#         with open(obj.file_name.path, 'r') as f:
#             reader = csv.reader(f)

#             for i, row in enumerate(reader):
#                 if i==0:
#                     pass
#                 else:
#                     row = "".join(row)
#                     row = row.replace(";", " ")
#                     row = row.split()
#                     print(row)
#                     print(type(row))
#             obj.activated = True
#             obj.save()

        

#     context = {
#         'form' : form,
#     }
    
    
#     return render(request, 'dataconversion/upload.html',context)

def listclients(request):
    clients = csv_client.objects.all()

    context = {
        'clients': clients
    }

    return render(request, 'dataconversion/listclients.html',context)
