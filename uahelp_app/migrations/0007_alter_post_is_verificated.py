# Generated by Django 4.0.2 on 2022-03-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uahelp_app', '0006_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_verificated',
            field=models.BooleanField(default=True),
        ),
    ]