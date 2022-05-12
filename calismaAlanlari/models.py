from django.db import models

# Create your models here.
class CalismaAlanlari(models.Model):



    calisma_icon = models.ImageField(upload_to="media/calismaIcon/%Y/%m/%d/",default='calismaAlanlariDefault/img.png',blank=True)
    calisma_title = models.CharField(max_length=50,blank=True)

    calisma_metni = models.TextField(blank=True)

    calisma_published_date = models.DateTimeField(auto_now_add=True)
    calisma_created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.calisma_title