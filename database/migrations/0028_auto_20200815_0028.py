# Generated by Django 3.0.8 on 2020-08-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0027_auto_20200815_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='files',
            field=models.FileField(blank=True, max_length=50, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='ask',
            name='image',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to='ques/'),
        ),
    ]