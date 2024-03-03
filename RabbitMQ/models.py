from mongoengine import Document, BooleanField, StringField
from Web_8.connect import connect
class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    is_message_sent = BooleanField(default=False)
    phone_number = StringField()