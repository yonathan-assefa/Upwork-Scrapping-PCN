# Generated by Django 4.0.4 on 2022-05-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_pcn_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=500)),
                ('lname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('email_old', models.CharField(max_length=500)),
                ('phone1', models.CharField(max_length=500)),
                ('phone1_old', models.CharField(max_length=500)),
                ('phone2', models.CharField(max_length=500)),
                ('phone2_old', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('zip', models.CharField(max_length=500)),
                ('community', models.CharField(max_length=500)),
            ],
        ),
    ]
