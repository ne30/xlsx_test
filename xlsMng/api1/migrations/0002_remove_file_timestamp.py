# Generated by Django 2.0 on 2020-12-21 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='timestamp',
        ),
    ]