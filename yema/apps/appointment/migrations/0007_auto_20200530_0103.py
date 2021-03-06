# Generated by Django 3.0.6 on 2020-05-30 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('appointment', '0006_auto_20200530_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('doctor', 'date', 'time')},
        ),
    ]
