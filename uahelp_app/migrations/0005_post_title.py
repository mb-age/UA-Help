# Generated by Django 4.0.2 on 2022-03-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uahelp_app', '0004_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Ttiittllee', max_length=200),
        ),
    ]
