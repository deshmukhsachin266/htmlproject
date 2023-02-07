# Generated by Django 4.1.5 on 2023-01-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('vname', models.CharField(max_length=40)),
                ('cname', models.CharField(max_length=40)),
                ('year', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
