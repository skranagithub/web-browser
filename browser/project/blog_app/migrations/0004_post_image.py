# Generated by Django 4.1.2 on 2023-02-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=None, max_length=400, null=True, upload_to='images/'),
        ),
    ]
