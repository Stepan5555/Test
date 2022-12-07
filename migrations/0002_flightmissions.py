# Generated by Django 4.1.3 on 2022-12-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightMissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uav_ID', models.CharField(blank=True, max_length=30)),
                ('uav_type', models.CharField(blank=True, max_length=30)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('cords', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
