from django.db import models
from django.contrib.auth.models import User, UserManager

#class User(models.Model):
 #   username=models.CharField(max_lenght=30)
  #  password=models.CharField(max_lenght=70)
  #  Email=models.models.EmailField(max_length=254)




class UserprofileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    protfoils_site = models.URLField(blank=True)
    ready = models.BooleanField(default=True)
    pic = models.ImageField()

    def __str__(self):
        return self.user.username