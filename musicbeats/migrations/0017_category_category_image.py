# Generated by Django 4.0.1 on 2022-01-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0016_singer_pishmahadi'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, default='profiles/user-defualt.png', null=True, upload_to='category/'),
        ),
    ]