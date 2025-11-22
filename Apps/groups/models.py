
from mongoengine import Document, StringField, IntField


class Groups(Document):
    meta = {"collection": "groups"}
    code_group = StringField(default="")
    level_group = StringField(default="")
    section_group = StringField(default="")
    amount_group = IntField()
# Create your models here.
