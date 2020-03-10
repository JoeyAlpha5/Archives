from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class userAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()





    def __str__(self):
        return self.user.username

def create_user_account(sender, **kwargs):
    if kwargs["created"]:
        new_user = userAccount.objects.create(user=kwargs["instance"])


class Residence(models.Model):
    user_account = models.ForeignKey(userAccount, on_delete=models.CASCADE)
    residence_name = models.CharField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return self.residence_name

class Unit(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    unit_no = models.CharField(max_length=150,default="")
    status = models.BooleanField(default=False)
    cell_no = models.CharField(max_length=12)
    objects=models.Manager()
    def __str__(self):
        return self.residence.residence_name+" "+self.unit_no


#listen for when a new user has been created, if so execute the create_user_account function
post_save.connect(create_user_account, sender=User)