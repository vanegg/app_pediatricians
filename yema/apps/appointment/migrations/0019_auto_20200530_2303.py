# Generated by Django 3.0.6 on 2020-05-31 04:03

from django.db import migrations, models
import django.utils.timezone
import yema.apps.appointment.validators


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0018_auto_20200530_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[yema.apps.appointment.validators.AppointmentValidator.validate_future_date]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('validating', 'validating'), ('approved', 'approved'), ('rejected', 'rejected'), ('completed', 'completed')], default='validating', max_length=15),
        ),
    ]