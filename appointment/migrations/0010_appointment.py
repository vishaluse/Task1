# Generated by Django 3.2.5 on 2021-07-18 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_auto_20210715_1611'),
        ('appointment', '0009_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('is_patient_name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=10)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
        ),
    ]
