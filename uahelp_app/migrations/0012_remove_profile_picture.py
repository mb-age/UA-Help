# Generated by Django 4.0.2 on 2022-03-24 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uahelp_app', '0011_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
