from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.



class Sektorler(models.Model):

    sektor_adi = models.CharField(max_length=50,blank=True)
    sektor_text = models.TextField(blank=True)
    sektor_img = models.ImageField(upload_to="media/sektorler/%Y/%m/%d/",default='sektorlerDefault/avrupa ofıs kale.jpg',blank=True)

    created_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.sektor_adi