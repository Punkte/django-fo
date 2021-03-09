from django.db import models
from django.conf import settings
from django.utils import timezone
from enum import Enum

class ContactStatus(Enum):
    RD = 'READ'
    SP = 'SPAM'
    UR = 'UNREAD'


class Contact(models.Model):
    contact_object = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
      max_length=2,
      choices=[(tag, tag.value) for tag in ContactStatus]
    )

    def __str__(self):
        return self.contact_object


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='formation/static/images/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title