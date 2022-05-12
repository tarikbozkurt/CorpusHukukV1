from django.db import models
from employee.models import Employee
# Create your models here.
class Vlog(models.Model):



    post_title = models.CharField(max_length=50, blank=True)
    post_tag = models.CharField(max_length=50,blank=True)
    post_text = models.TextField(blank=True)
    post_image=models.ImageField(upload_to="postsImages/%Y/%m/%d", blank=True)

    owner=models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True)
    post_published_date=models.DateTimeField(auto_now_add=True,blank=True)
    post_created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title



