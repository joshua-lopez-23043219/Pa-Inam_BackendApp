from django.db import models

from mongoengine import Document, StringField, IntField


class Notes (Document):
    meta = {"collection": "notes"}

    registration_id = StringField(required=True)
    subject_id    = StringField(required=True)
    first_partial    = IntField(required=True)
    second_partial    = IntField(required=True)
    first_semester    = IntField(required=True)
    third_partial    = IntField(required=True)
    quarter_partial   = IntField(required=True)
    second_semester    = IntField(required=True)
    final_grade    = StringField(required=True)
    special_note = StringField(default="")


# Create your models here.
