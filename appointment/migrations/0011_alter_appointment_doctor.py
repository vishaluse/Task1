# Generated by Django 3.2.5 on 2021-07-19 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210715_1611'),
        ('appointment', '0010_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.doctor'),
        ),
    ]
