from django.db import models

# Burada standart tüm sayfalarda mevcut olacak olan datalarımıza yer vereceğiz

class PageSettings(models.Model):

    page_tag=models.CharField(max_length=50,blank=True)

    page_title = models.CharField(max_length=100,blank=True)

    page_img=models.ImageField(upload_to="pageImage/%Y/%m/%d/",blank=True,default='pageDefault/paper-2.jpg')

    available = models.BooleanField(default=True)

    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_title