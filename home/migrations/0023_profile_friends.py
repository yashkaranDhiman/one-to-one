# Generated by Django 4.2.4 on 2023-10-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='my_followers', to='home.friend'),
        ),
    ]
