from django.db import models

# Create your models here.
class firmaBilgi(models.Model):
    firma_adi = models.CharField(max_length=50,blank=True)

    firma_kurulus_tarihi = models.DateTimeField(blank=True)


    firma_logo = models.ImageField(upload_to="firmaBilgi/%Y/%m/%d",blank=True,default='firmaLogoDefault/logo-corpus.svg')
    firma_email = models.EmailField(blank=True)
    firma_telefon = models.CharField(max_length=18,blank=True)
    firma_lokasyon = models.CharField(max_length=500,blank=True)

    firma_created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firma_adi


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email
