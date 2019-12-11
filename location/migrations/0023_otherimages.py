# Generated by Django 2.2.8 on 2019-12-08 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0022_claimrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('apartment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='location.Apartment')),
            ],
        ),
    ]
