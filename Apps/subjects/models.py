from django.db import models
from mongoengine import Document, StringField, IntField

class Subjects(Document):
    meta = {"collection": "subjects"}

    code_subject = StringField(required=True)
    name_subject= StringField(default="")
    period_subject = StringField(default="")
    level_subjects = StringField(default="")
# Create your models here.
