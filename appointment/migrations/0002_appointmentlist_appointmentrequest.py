# Generated by Django 3.2.5 on 2021-07-18 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210715_1611'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='account.patient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ManyToManyField(blank=True, related_name='appoint', to='appointment.Appointment')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='account.doctor')),
            ],
        ),
    ]
