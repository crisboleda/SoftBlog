# Generated by Django 3.0.1 on 2019-12-31 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
