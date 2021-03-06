# Generated by Django 3.1.3 on 2020-11-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
