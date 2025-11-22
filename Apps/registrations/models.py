from datetime import datetime, timezone

from django.db import models
from mongoengine import Document, StringField, IntField, DateTimeField


class Registration(Document):
    meta = {"collection": "registrations"}

    code_registration = StringField(default="")
    date_registration= DateTimeField(default=lambda:datetime.now(timezone.utc))
    mode_registration= StringField(default="")
    level_registration= StringField(default="")
    student_id= StringField(required=True)
    group_id= StringField(required=True)
    tutor_id= StringField(required=True)
# Create your models here.
