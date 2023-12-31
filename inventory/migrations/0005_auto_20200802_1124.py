# Generated by Django 3.0.7 on 2020-08-02 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200711_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='handshape',
            name='bend1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='handshape',
            name='bend2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='handshape',
            name='bend3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='handshape',
            name='bend4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='handshape',
            name='bend5',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='handshape',
            name='handshape',
            field=models.CharField(default='', max_length=20, verbose_name='Handshape'),
        ),
        migrations.AddField(
            model_name='handshape',
            name='mainbend',
            field=models.CharField(default='', max_length=20, verbose_name='Main Bend'),
        ),
        migrations.AddField(
            model_name='handshape',
            name='specialfingers',
            field=models.CharField(default='', max_length=20, verbose_name='Special Fingers'),
        ),
        migrations.AddField(
            model_name='handshape',
            name='thumbpos',
            field=models.CharField(default='', max_length=20, verbose_name='Thumb Position'),
        ),
    ]
