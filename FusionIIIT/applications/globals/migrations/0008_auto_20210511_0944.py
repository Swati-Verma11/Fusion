# Generated by Django 3.1.5 on 2021-05-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0007_auto_20210509_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('NEW', 'NEW')], default='PRESENT', max_length=50),
        ),
    ]
