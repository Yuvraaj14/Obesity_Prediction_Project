# Generated by Django 5.1.3 on 2024-11-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v1', models.CharField(max_length=200)),
                ('v2', models.CharField(max_length=200)),
                ('v3', models.CharField(max_length=200)),
                ('v4', models.CharField(max_length=200)),
                ('v5', models.CharField(max_length=200)),
            ],
        ),
    ]