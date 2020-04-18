from django.db import models
from django.utils import timezone

# Create your models here.

class blogContents(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, max_length=255, )
    content = models.TextField()
    updataTime = models.DateTimeField(default=timezone.now)
    timesOfReply = models.IntegerField()
    timesOfRead = models.IntegerField()


class commentContent(models.Model):
    id = models.AutoField(primary_key=True)
    blogId = models.IntegerField()
    commentTime = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    name = models.CharField(blank=False, max_length=255)
    email = models.EmailField()