# Generated by Django 3.0 on 2020-12-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyWorkStatus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exfd',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]