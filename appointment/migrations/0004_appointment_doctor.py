# Generated by Django 3.2.5 on 2021-07-18 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210715_1611'),
        ('appointment', '0003_auto_20210718_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.doctor'),
        ),
    ]
