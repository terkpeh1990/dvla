# Generated by Django 3.2.6 on 2021-09-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0011_auto_20210907_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
