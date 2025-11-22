from django.db import models
from mongoengine import Document, StringField, DateTimeField, IntField

class Documents(Document):
    meta = {"collection": "documents"}

    code_document = StringField(required=True)
    name_document = StringField(required=True)
    file = StringField(required=True)
    student_id = StringField(required=True)




# Create your models here.
