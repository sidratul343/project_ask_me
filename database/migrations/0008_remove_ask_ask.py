# Generated by Django 3.0.8 on 2020-08-05 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_ask_ask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ask',
            name='ask',
        ),
    ]