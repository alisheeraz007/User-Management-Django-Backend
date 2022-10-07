from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50, default="")
    age = models.CharField(max_length=50,default="")
    additionalInfo = models.CharField(max_length=300)
    dateOfBirth = models.DateField()
    profileImage = models.ImageField(upload_to='shop/images', default="")
    
    def __str__(self):
        return self.user_name