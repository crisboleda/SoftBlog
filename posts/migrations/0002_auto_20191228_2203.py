# Generated by Django 3.0.1 on 2019-12-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caterory',
            name='name_category',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]