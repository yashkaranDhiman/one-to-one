# Generated by Django 4.2.4 on 2023-10-23 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_profile_followers_profile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
    ]
