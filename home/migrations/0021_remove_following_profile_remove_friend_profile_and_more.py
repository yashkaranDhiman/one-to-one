# Generated by Django 4.2.4 on 2023-10-23 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_profile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatMessages',
        ),
        migrations.DeleteModel(
            name='Following',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
