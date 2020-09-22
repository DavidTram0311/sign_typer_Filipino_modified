# Generated by Django 3.0.7 on 2020-09-17 08:23

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20200813_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='leftMotionSequence',
            field=django_mysql.models.ListTextField(models.CharField(max_length=1000), default=[], size=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sign',
            name='rightMotionSequence',
            field=django_mysql.models.ListTextField(models.CharField(max_length=1000), default=[], size=10),
            preserve_default=False,
        ),
    ]
