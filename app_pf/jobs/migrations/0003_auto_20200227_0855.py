# Generated by Django 2.0.2 on 2020-02-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200227_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(default='ENTER URL'),
        ),
    ]
