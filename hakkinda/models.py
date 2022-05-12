from django.db import models

# Create your models here.
class Hakkinda(models.Model):

    hakkinda_title = models.CharField(max_length=50,blank=True)
    hakkinda_text= models.TextField(blank=True)
    hakkinda_created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hakkinda_title

class firmaOzellikleri(models.Model):

    firmaOzellik_title=models.CharField(max_length=50,blank=True)
    firmaOzellik_text=models.TextField(blank=True)
    firmaOzellik_icon=models.ImageField(upload_to="media/firmaOzellikleriIcons/%Y/%m/%d/",blank=True)
    firmaOzellik_adet=models.IntegerField(blank=True)
    firmaOzellik_created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firmaOzellik_title
