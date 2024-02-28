from mongoengine import Document
from mongoengine.fields import ReferenceField, ListField, StringField


class Author(Document):
    description = StringField()
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()


class Quote(Document):
    quote = StringField()
    tags = ListField(StringField())
    author = ReferenceField(Author)