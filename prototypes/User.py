import mongoengine
from mongoengine import StringField, IntField, Document

class User(Document):
    studentid = StringField(required=True)
    name = StringField(max_length=50)
    age = IntField()
    def _init__(self, id, name, age):
        self.studentid = id,
        self.name = name
        self.age = age
