# Generated by Django 4.1.7 on 2023-03-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naukri', '0002_alter_desc_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='desc',
            name='day',
            field=models.IntegerField(default= 1),
        ),
    ]
