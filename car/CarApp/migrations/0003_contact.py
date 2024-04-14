# Generated by Django 5.0.1 on 2024-04-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0002_remove_car_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'Cantact',
            },
        ),
    ]
