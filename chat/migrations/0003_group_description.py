# Generated by Django 3.0.1 on 2020-01-07 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200106_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
