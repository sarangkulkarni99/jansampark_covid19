# Generated by Django 3.0.5 on 2020-04-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0002_auto_20200412_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailer',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='retailer',
            name='lat',
            field=models.CharField(default='0', max_length=15),
        ),
        migrations.AddField(
            model_name='retailer',
            name='long',
            field=models.CharField(default='0', max_length=15),
        ),
    ]
