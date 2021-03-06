# Generated by Django 3.0.6 on 2020-05-31 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'doctor', 'verbose_name_plural': 'doctors'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'patient', 'verbose_name_plural': 'patients'},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
