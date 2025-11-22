from django.db import models
from mongoengine import Document , StringField, EmailField, IntField

class Student(Document):
    meta = {"collection": "students"}
    code_student = StringField(required=True, default="")
    name_student= StringField( default="")
    surname_student = StringField( default="")
    birthday_student= StringField( default="")
    phone_student= StringField( default="")
    email_student= EmailField( default="")

# Create your models here.
