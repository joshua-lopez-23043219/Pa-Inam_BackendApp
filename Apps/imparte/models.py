from django.db import models
from mongoengine import Document, StringField

class Imparte(Document):
    meta = {"collection": "imparte"}
    hour = StringField(default="")
    group_id = StringField(required=True)
    subject_id = StringField(required=True)
    teacher_id = StringField(required=True)
# Create your models here.
