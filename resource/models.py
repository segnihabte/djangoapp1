from random import choices
from re import T
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

class Username(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length =200)
    Gender = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    demo_link = models.CharField(max_length=200, null=True)
    source_link = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)

class personDiscription(models.Model):
    VOTE_TYPE = (
        ('Good', 'Up Vote'),
        ('Bad', 'Down Vote'),
    )
    hairColor=models.CharField(max_length=200)
    Behavior=models.CharField(max_length=200, choices=VOTE_TYPE)
    Username = models.ForeignKey(Username, on_delete=models.CASCADE)
    def __str__(self):
        return self.Behavior
class jobDiscription(models.Model):
    job=models.ManyToManyField(personDiscription, blank=True)