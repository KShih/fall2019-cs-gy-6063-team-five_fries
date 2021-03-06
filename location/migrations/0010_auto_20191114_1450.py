# Generated by Django 2.2.6 on 2019-11-14 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0009_auto_20191113_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='landlord',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='landlord_apartment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartment',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_apartment_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
