# Generated by Django 2.2.6 on 2019-11-24 18:56

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('external', '0006_auto_20191121_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='NYC311Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', localflavor.us.models.USZipCodeField(db_index=True, max_length=10)),
                ('complaint_type', models.CharField(max_length=255)),
                ('complaint_level', models.IntegerField()),
                ('total_complaints_query_zip', models.IntegerField()),
                ('closed_complaints_query_zip', models.IntegerField()),
                ('percentage_complaints_closed', models.FloatField()),
                ('max_complaints', models.IntegerField()),
                ('max_complaints_zip', localflavor.us.models.USZipCodeField(max_length=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]