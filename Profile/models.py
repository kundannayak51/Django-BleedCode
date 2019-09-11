from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #user = models.OneToOneField(User,on_delete=True)
    institution = models.CharField(max_length = 50, default = "", blank = True)
    country = models.CharField(max_length = 30, default = "", blank = True)
    rating = models.FloatField(default = 0.0,)
    profilePicture = models.ImageField(default = "", blank = True,upload_to='images/profilepic')
    noOfSubmissions = models.IntegerField(default = 0)
    probSolved = models.CharField(max_length=20000,default = "", blank = True)
    probAttemped = models.CharField(max_length=20000,default = "", blank = True)


    def __str__(self):
        return self.user.username
    #def addProbSolved(problem):
        #if str(problem) in probAttemped:
            #removeProbAttempted(problem)
        #probSolved = probSolved + str(problem)

    #def removeProbAttempted(problem):
        #x = probAttemped.split(",")

    '''def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()

    post_save.connect(create_profile, sender=User)

    def __unicode__(self):
        return self.user.username'''

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        #user = instance
        if created:
            Profile.objects.create(user=instance)



    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
