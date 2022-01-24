# Generated by Django 4.0.1 on 2022-01-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0011_remove_album_song_song_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hesohal',
            name='album',
        ),
        migrations.AddField(
            model_name='hesohal',
            name='album',
            field=models.ManyToManyField(blank=True, to='musicbeats.Album'),
        ),
        migrations.RemoveField(
            model_name='hesohal',
            name='song',
        ),
        migrations.AddField(
            model_name='hesohal',
            name='song',
            field=models.ManyToManyField(blank=True, to='musicbeats.Song'),
        ),
    ]
