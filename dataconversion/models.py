from django.db import models

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs', blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File ID : {self.id} - {self.file_name}"



class csv_client(models.Model):
    CLIENTNUMBER = models.CharField(max_length=25, blank=True, null=True)
    EntityType = models.CharField(max_length=15, blank=True, null=True)
    ClientName = models.CharField(max_length=200, blank=True, null=True)
    UnitDescription = models.CharField(max_length=100, blank=True, null=True)
    Street = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=100, blank=True, null=True)
    State_Prov = models.CharField(max_length=100, blank=True, null=True)
    Country = models.CharField(max_length=25, blank=True, null=True)
    Fax_Number = models.CharField(max_length=60, blank=True, null=True)
    EMail = models.CharField(max_length=100, blank=True, null=True)
    URL = models.CharField(max_length=60, blank=True, null=True)
    Zip_Code = models.CharField(max_length=25, blank=True, null=True)
    Telephone_Number = models.CharField(max_length=60, blank=True, null=True)
    Date_Acquired = models.DateField(blank=True, null=True)
    CountryCode = models.CharField(max_length=25, blank=True, null=True)
    Industry = models.CharField(max_length=100, blank=True, null=True)
    DateEntered = models.DateField(blank=True, null=True)
    ClientType = models.CharField(max_length=25, blank=True, null=True)
    AccountOfficer = models.CharField(max_length=60, blank=True, null=True)
    ContactPerson = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.ClientName}"
