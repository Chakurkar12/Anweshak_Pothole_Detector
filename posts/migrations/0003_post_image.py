# Generated by Django 4.2.1 on 2023-05-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
