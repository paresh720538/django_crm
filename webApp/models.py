from django.db import models

# Create your models here.
#we have to pass the record model in the admin field

class Record(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name =  models.CharField(max_length=100,  null=True)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    province = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    
    
    def __str__(self):

        return self.first_name + "   " + self.last_name
