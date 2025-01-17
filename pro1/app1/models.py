'''
from mongoengine import Document, StringField, DecimalField

class Student(Document):
    id = DecimalField(primary_key=True)
    name = StringField(max_length=100)
    marks = DecimalField()
'''
from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    marks = models.FloatField()