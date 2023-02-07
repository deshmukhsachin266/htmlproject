# Generated by Django 4.1.5 on 2023-01-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
