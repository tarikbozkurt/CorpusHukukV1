from django.db import models

# Create your models here.



class Employee(models.Model):

    user_name = models.CharField(max_length=50,blank=True)
    user_surname = models.CharField(max_length=50,blank=True)
    user_password = models.CharField(max_length=15,blank=True)



    def __str__(self):
        return  self.user_name +" "+ self.user_surname


class EmployeeInformations(models.Model):
    user_name=models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True)
    unvan = models.CharField(max_length=50, blank=True)
    user_email = models.EmailField(max_length=50, blank=True)
    user_phone = models.CharField(max_length=12, blank=True)

    about_user = models.TextField(blank=True)

    user_image = models.ImageField(upload_to="userProfile/%Y/%m/%d", blank=True)

    def __str__(self):
        return  self.unvan + " " + self.user_name.user_name

