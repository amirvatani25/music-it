# Generated by Django 4.0.1 on 2022-01-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0015_alter_album_singer'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='pishmahadi',
            field=models.BooleanField(default=False),
        ),
    ]
