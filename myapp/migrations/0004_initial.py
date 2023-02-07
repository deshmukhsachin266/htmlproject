# Generated by Django 4.1.5 on 2023-01-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0003_delete_automobile_delete_person'),
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
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveBigIntegerField()),
            ],
        ),
    ]
