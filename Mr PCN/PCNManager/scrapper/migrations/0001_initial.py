# Generated by Django 4.0.4 on 2022-04-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PCN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcn', models.CharField(max_length=14)),
                ('owner', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(max_length=255)),
                ('control_number', models.CharField(max_length=30)),
                ('subdivision', models.CharField(max_length=255)),
                ('legal_description', models.TextField()),
            ],
        ),
    ]