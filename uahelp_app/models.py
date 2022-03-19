from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, TextField, URLField, ForeignKey, CASCADE, BooleanField, DateTimeField


# Create your models here.

class AccountType(Model):
    type = CharField(max_length=40)

    def __str__(self):
        return self.type



class Country(Model):
    name = CharField(max_length=40)

    def __str__(self):
        return self.name



class Profile(Model):
    name = CharField(max_length=200, help_text='Your name/nickname/company name etc.')
    account_type = ForeignKey(to=AccountType, on_delete=CASCADE)
    user = ForeignKey(to=User, on_delete=CASCADE)
    country = ForeignKey(to=Country, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



class Post(Model):
    profile = ForeignKey(to=Profile, on_delete=CASCADE)
    content = TextField()
    is_verificated = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content



class Link(Model):
    profile = ForeignKey(to=Profile, on_delete=CASCADE)
    content = URLField()

    def __str__(self):
        return self.content




