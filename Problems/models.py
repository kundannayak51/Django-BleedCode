from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class ProblemSet(models.Model):
    # pid = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10)
    no_of_submissions = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0.0)
    tags = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    constraints = models.TextField(default="")
    inputDesc = models.TextField(default="")
    outputDesc = models.TextField(default="")
    problemSetter = models.CharField(max_length=30, default="")
    problemTester = models.CharField(max_length=30, default="")
    publishDate = models.DateField(default=datetime.date.today)
    timeLimit = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.title


class Submissions(models.Model):
    submission_id=  models.AutoField(primary_key=True)
    problem_sub = models.ForeignKey(ProblemSet, on_delete=models.CASCADE)
    user_sub = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("User"), on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='Submission/')
    ac_or_not = models.BooleanField(default=False)
    language_submitted = models.TextField(default="c")

    def __unicode__(self):
        return self.submission_id
