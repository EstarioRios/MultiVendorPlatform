# Generated by Django 5.1.4 on 2025-02-26 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationSystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='store_industry',
        ),
    ]
