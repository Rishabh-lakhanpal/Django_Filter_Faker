# Generated by Django 4.1.3 on 2022-11-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
