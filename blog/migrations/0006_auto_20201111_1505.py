# Generated by Django 3.1.3 on 2020-11-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201111_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
