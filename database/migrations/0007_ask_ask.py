# Generated by Django 3.0.8 on 2020-08-05 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_ask_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='ask',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='database.profile'),
            preserve_default=False,
        ),
    ]
