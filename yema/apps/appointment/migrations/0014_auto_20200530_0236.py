# Generated by Django 3.0.6 on 2020-05-30 07:36

from django.db import migrations, models
import django.utils.timezone
import yema.apps.appointment.validators


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0013_auto_20200530_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[yema.apps.appointment.validators.AppointmentValidator.validate_future_date]),
        ),
    ]
