from datetime import datetime, timezone
from django.db import models
from mongoengine import Document, StringField, EmailField
from rest_framework.fields import DateTimeField


class Tutor(Document):
    meta = {"collection": "tutors"}

    code_tutor = StringField(required=True, default="")
    name_tutor= StringField( default="")
    surname_tutor= StringField( default="")
    birthday_tutor= StringField( default="")
    phone_tutor= StringField( default="")
    email_tutor= EmailField( default="")
    address_tutor= DateTimeField(default=lambda: datetime.now(timezone.utc))

    #Create your models here.
