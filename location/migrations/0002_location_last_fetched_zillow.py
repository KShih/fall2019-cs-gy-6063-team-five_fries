# Generated by Django 2.2.6 on 2019-11-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='last_fetched_zillow',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
