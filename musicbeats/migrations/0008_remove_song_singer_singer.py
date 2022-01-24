# Generated by Django 4.0.1 on 2022-01-17 09:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0007_alter_category_name_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='singer',
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('name', models.CharField(max_length=290)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='musicbeats.song')),
            ],
        ),
    ]