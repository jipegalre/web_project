# Generated by Django 5.0.5 on 2024-10-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blog_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
