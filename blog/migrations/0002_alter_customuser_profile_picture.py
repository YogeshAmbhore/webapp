# Generated by Django 4.2.5 on 2023-09-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='blog/media/default.webp', null=True, upload_to='blog/profile/'),
        ),
    ]