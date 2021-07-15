# Generated by Django 3.2.5 on 2021-07-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210715_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default='blog.png', null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]