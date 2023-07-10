# Generated by Django 4.2.3 on 2023-07-10 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('addres', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=10)),
                ('entry', models.DateField(default=datetime.date.today)),
                ('out', models.DateField(default=datetime.date.today)),
                ('holidays', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
