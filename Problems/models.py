from __future__ import unicode_literals
import datetime
from django.db import models


# Create your models here.
class ProblemSet(models.Model):
    # pid = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10)
    submissions = models.IntegerField(default=0)
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


from django.db import models

# Create your models here.