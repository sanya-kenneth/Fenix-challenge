# Generated by Django 2.2.6 on 2019-10-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fenixapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='momorequest',
            name='callback_id',
            field=models.TextField(null=True),
        ),
    ]
