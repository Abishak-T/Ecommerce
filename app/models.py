from django.db import models

# Create your models here.

class AppModel(models.Model):
    choose_img=models.ImageField(upload_to="images",blank=True,null=True)
    price=models.TextField()
    category=models.TextField(null=True)
    
    
class SubModel(models.Model):
    category=models.TextField(null=True)

    imgg=models.ImageField(upload_to="images",blank=True,null=True)
    prodname=models.TextField()
    prodprice=models.TextField()
    imgone=models.ImageField(upload_to="images",blank=True,null=True)
    imgtwo=models.ImageField(upload_to="images",blank=True,null=True)
    desc=models.TextField(null=True)
    
    
class SignupModel(models.Model):
    signname=models.TextField(null=True)  
    signemail=models.EmailField(null=True)
    signpass=models.TextField(null=True)  
    signconpass=models.TextField(null=True)
    
    
    