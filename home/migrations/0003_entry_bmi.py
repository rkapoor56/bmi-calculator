# Generated by Django 3.1.5 on 2021-02-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210129_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='bmi',
            field=models.FloatField(null=True),
        ),
    ]
