# Generated by Django 5.0.2 on 2024-04-08 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='Cars/logo/')),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Cars/')),
                ('type', models.CharField(max_length=255)),
                ('time', models.FloatField()),
                ('power', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('engine', models.CharField(choices=[('BENZIN', 'BENZIN'), ('ELEKTR', 'ELEKTR'), ('GIBRID', 'GIBRID')], default='BENZIN', max_length=50)),
                ('price', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarApp.brand')),
            ],
            options={
                'verbose_name_plural': 'Car',
            },
        ),
    ]
