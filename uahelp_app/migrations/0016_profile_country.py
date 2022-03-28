# Generated by Django 4.0.2 on 2022-03-25 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uahelp_app', '0015_remove_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uahelp_app.country'),
        ),
    ]