from django.db import models


# Create your models here.

class LoginUser(models.Model):
    mobileNo = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    #json = models.JSONField()

    def __str__(self):
        return self.mobileNo


    