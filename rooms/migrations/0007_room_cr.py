# Generated by Django 2.2.5 on 2019-11-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20191108_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='cr',
            field=models.DateTimeField(null=True),
        ),
    ]
