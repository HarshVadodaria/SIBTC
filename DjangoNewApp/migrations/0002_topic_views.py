# Generated by Django 3.1.4 on 2020-12-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoNewApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
