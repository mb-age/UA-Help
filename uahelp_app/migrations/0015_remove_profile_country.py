# Generated by Django 4.0.2 on 2022-03-25 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uahelp_app', '0014_alter_profile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
    ]