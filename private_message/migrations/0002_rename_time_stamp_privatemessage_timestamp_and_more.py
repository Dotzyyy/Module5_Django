# Generated by Django 5.0.6 on 2024-06-19 19:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_message', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatemessage',
            old_name='time_stamp',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='privatemessage',
            name='cc',
            field=models.ManyToManyField(blank=True, related_name='cc_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]