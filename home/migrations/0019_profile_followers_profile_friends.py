# Generated by Django 4.2.4 on 2023-10-23 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_profile_followers_remove_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='my_friends', to='home.following'),
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='my_followers', to='home.friend'),
        ),
    ]
