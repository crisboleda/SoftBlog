# Generated by Django 3.0.1 on 2019-12-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='users/pictures'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]