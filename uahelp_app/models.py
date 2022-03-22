import random
from io import BytesIO

import requests
from django.contrib.auth.models import User
from django.core.files import File
from django.db.models import Model, CharField, TextField, URLField, ForeignKey, CASCADE, BooleanField, DateTimeField, \
    ImageField, IntegerField
# Create your models here.
from django.utils import timezone


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
    DONATION_TYPE = 0
    PROMOTION_TYPE = 1
    SHELTER_TYPE = 2
    EVENT_TYPE = 3
    POST_TYPES = (
        (DONATION_TYPE, "Dotacja"),
        (PROMOTION_TYPE, "Promocja"),
        (SHELTER_TYPE, "Schronienie"),
        (EVENT_TYPE, "Wydarzenie")
    )

    profile = ForeignKey(to=Profile, on_delete=CASCADE)
    created_at = DateTimeField(default=timezone.now)
    title = CharField(max_length=200)
    content = TextField()
    type = IntegerField(choices=POST_TYPES, default=DONATION_TYPE, help_text="Rodzaj pomocy")
    dotation_amount = IntegerField(default=random.randint(10, 100000), help_text="Wysokość dotacji w PLN")
    cover_image = ImageField(upload_to='post_images', null=True)
    is_verificated = BooleanField(default=False)

    def get_image_from_url(self, url):
        resp = requests.get(url)
        fp = BytesIO()
        fp.write(resp.content)
        file_name = url.split("/")[-1]  # There's probably a better way of doing this but this is just a quick example
        self.cover_image.save(file_name, File(fp))

    def __str__(self):
        return self.content


class Link(Model):
    profile = ForeignKey(to=Profile, on_delete=CASCADE)
    content = URLField()

    def __str__(self):
        return self.content
