from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class Product(models.Model):
#     user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
#     desc = models.CharField(max_length=50,null=True,blank=True)
#     price = models.DecimalField(max_digits=5,decimal_places=2)
#     createdTime=models.DateTimeField(auto_now_add=True)
#     fields =['desc','price']
 
#     def __str__(self):
#            return self.desc



class Gal(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.title

