# Generated by Django 3.2 on 2021-04-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_form', '0005_auto_20210428_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
