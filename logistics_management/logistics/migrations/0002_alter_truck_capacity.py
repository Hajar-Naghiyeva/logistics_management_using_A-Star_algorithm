# Generated by Django 4.2.7 on 2023-12-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logistics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="truck",
            name="capacity",
            field=models.IntegerField(default=10),
        ),
    ]
