from django.db import models
from mongoengine import Document, StringField, IntField, EmailField


class Teachers(Document):
    meta = {"collection": "teachers"}

    code_teacher= StringField(required=True, default="")
    name_teacher= StringField( default="")
    surname_teacher= StringField( default="")
    phone_teacher=StringField( default="")
    email_teacher= EmailField( default="")
    address_teacher= StringField( default="")
    area_teacher= StringField( default="")

# Create your models here.
