# Generated by Django 3.0.6 on 2020-05-30 05:19

from django.db import migrations, models
import django.utils.timezone
import yema.apps.appointment.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('appointment', '0004_auto_20200529_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[yema.apps.appointment.validators.AppointmentValidator.validate_future_date]),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('doctor', 'date')},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='hour',
        ),
    ]
