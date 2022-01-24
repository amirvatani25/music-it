# Generated by Django 4.0.1 on 2022-01-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0005_alter_album_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song',
            new_name='song128',
        ),
        migrations.AddField(
            model_name='song',
            name='song320',
            field=models.FileField(default=1, upload_to='musics/'),
            preserve_default=False,
        ),
    ]