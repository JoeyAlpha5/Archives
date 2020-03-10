from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.core.mail import send_mail
# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.subject_name

class pastPaper(models.Model):
    Description = models.CharField(max_length=100,default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True )
    _file = CloudinaryField(resource_type='auto',blank=True,default="")
    objects = models.Manager()

class Slide(models.Model):
    Description = models.CharField(max_length=100,default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True )
    _file = CloudinaryField(resource_type='auto',blank=True,default="")
    objects = models.Manager()


class Video(models.Model):
    Description = models.CharField(max_length=100,default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    link = models.URLField()
    objects = models.Manager()

    def __str__(self):
        return self.Description


class Announcement(models.Model):
    announcement = models.CharField(max_length=100,default="")
    date = models.DateTimeField(auto_now_add=True )
    objects = models.Manager()

    def __str__(self):
        return self.announcement



    
def create_user_account(sender, **kwargs):
    if kwargs["created"]:
        print("announcement is created")
        print(kwargs["instance"].announcement)
        announcement = kwargs["instance"].announcement
        user_emails = []
        users = User.objects.all()
        for i in users:
            user_emails.append(i.email)
        send_mail('New EduChamp Announcement',announcement , 'smtp@conveniencemp.co.za', user_emails)
    
    
#listen for when a new user has been created, if so execute the create_user_account function
post_save.connect(create_user_account, sender=Announcement)
