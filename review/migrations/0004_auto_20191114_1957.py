# Generated by Django 2.2.6 on 2019-11-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
