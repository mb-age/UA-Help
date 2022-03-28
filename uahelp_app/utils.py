import random
from datetime import timedelta
from pprint import pprint

import requests
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from uahelp_app.models import Post, Profile, User, AccountType, Country


def generate_fake_profile():
    api_data = requests.get('https://randomuser.me/api/').json()['results'][0]

    user = User.objects.get_or_create(
        username=api_data['login']['username'],
        email=api_data['email'],
        first_name=api_data['name']['first'],
        last_name=api_data['name']['last'],
        password=make_password('babcia11'),
    )[0]
    profile = Profile.objects.get_or_create(
        user=user,
        name=f'{api_data["name"]["title"]} {api_data["name"]["first"]}',
        account_type=AccountType.objects.last(),
        country=Country.objects.get_or_create(name=api_data['location']['country'])[0],
    )[0]

    return profile


def get_news():
    API_KEY = settings.GOPERIGON_API_KEY
    ALL_URL = f"https://api.goperigon.com/v1/all?apiKey={API_KEY}"

    resp = requests.get(f"{ALL_URL}&q=ukraine war%language=pl&from=2022-02-01&sortBy=relevance&size=1").json()
    article = resp['articles'][0]
    pprint(article)
    return article


def generate_random_post():
    article = get_news()

    # Preparing initial data for faked post
    initial = {
        "profile": generate_fake_profile(),
        "title": article['title'],
        "content": article['summary'],
        "type": random.randint(0, 3),
        "is_verificated": True,
        "created_at": timezone.now() - timedelta(days=random.randint(30, 100))
    }
    post = Post(**initial)
    post.get_image_from_url(article['imageUrl'])
    post.save()
