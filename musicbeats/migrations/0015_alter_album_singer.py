# Generated by Django 4.0.1 on 2022-01-19 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0014_hesohal_hesohal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='musicbeats.singer'),
        ),
    ]
