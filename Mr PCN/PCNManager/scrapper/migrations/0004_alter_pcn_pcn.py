# Generated by Django 4.0.4 on 2022-05-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0003_directory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcn',
            name='pcn',
            field=models.CharField(max_length=255),
        ),
    ]
