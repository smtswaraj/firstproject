# Generated by Django 4.1.7 on 2023-03-19 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naukri', '0009_alter_desc_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desc',
            name='day',
        ),
    ]