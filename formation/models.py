from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
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

class Skills(Enum):
    JAVA = 'JAVA'
    CPP = 'C++'
    PYTH = 'PYTHON'
    JS = 'JAVASCRIPT'
    HTML = 'HTML'
    CSS = 'CSS'

class Experience(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class CV(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    skills = models.ManyToManyField('Skill', through='CVSkill')
    experiences = models.TextField(null=True, blank=True)

    def get_skills(self):
        return ",".join([str(p) for p in self.parent.all()])

    
    def __str__(self):
        return self.name + ' ' + self.first_name


class CVSkill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

# class CVExperience(models.Model):
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE), 
#     experience = models.ForeignKey(Experience, on_delete=models.CASCADE)