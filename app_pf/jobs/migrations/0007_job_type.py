# Generated by Django 2.2.12 on 2020-10-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20200907_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]