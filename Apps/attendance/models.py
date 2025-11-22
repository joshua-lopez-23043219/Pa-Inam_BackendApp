from datetime import datetime, timezone

from django.db import models
from mongoengine import Document, StringField, DateTimeField, IntField


class Attendance(Document):
    meta = {"collection": "attendance"}

    registration_id = StringField(required=True)
    subject_id = StringField(required=True)
    date = DateTimeField(default=lambda: datetime.now(timezone.utc))
    quantity = IntField()



# Create your models here.
